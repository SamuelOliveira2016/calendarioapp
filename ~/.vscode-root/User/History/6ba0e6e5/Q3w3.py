from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

from datetime import datetime, timedelta
import datetime
from django.core.exceptions import ValidationError
from .google_calendar import fetch_holidays

from .schedule_validators import (is_aula_disponivel_no_dia_letivo, 
                                  is_infraestrutura_disponivel, 
                                  is_professor_disponivel, 
                                  is_carga_horaria_respeitada)

def validar_data(value):
    '''Função que impede a data ser retroativa à data atual'''
    hoje = timezone.now().date()
    if value < hoje:
        raise ValidationError("A data não pode ser retroativa. Por favor selecione o dia atual ou uma data futura")

class Evento(models.Model):
    '''Modelo para cria eventos no decorrer de uma linha do tempo, 
    utiliza uma função de validação de datas, para funcionar é necessário o nome
    do evento e data'''
    descricao = models.CharField(max_length=100)
    data_evento = models.DateField(validators=[validar_data], default = "1920/02/02")

    def __str__(self):
        return f"Nome do Evento: {self.descricao}"

class CadastroEscola(models.Model):
    '''Modelo para cadastrar a escola os 
    dados necessários são o id, o nome da escola e seu respectivo número de unidade'''
    descricao = models.CharField(max_length=100)
    unidade = models.CharField(max_length = 3)

    def __str__(self):
        return self.unidade

class CapacidadesFundamentos(models.Model):
    '''Modelo para alocação de capacidades ou fundamentos técnicos
    e capacidades Socioemocionais, os dados relacionados são descrição e tipo que deverá 
    ser escolhido entre as duas opções possiveis'''
    descricao = models.CharField(max_length=100)

    TIPO_CHOICE = ((1,'Fundamentos'),
                   (2, 'Técnica'),
                   (3, 'Socioemocional'))
    
    tipo = models.IntegerField(choices=TIPO_CHOICE)

    def __str__(self):
        return self.descricao
    

class UnidadeCurricular(models.Model):
    '''Modelo para alocação de unidades curriculares, possui uma chave estrangeira
    do modelo CapacidadesFundamentos, os dados necessários sâo descrição,
    carga horaria total da unidade e a cor(A cor é para representação no Frond-end)'''
    descricao = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(blank=True, null=True)
    capacidadeFundamentos = models.ForeignKey(CapacidadesFundamentos, on_delete=models.CASCADE, blank=True, null=True)
    cor = models.CharField(max_length=10, blank=True)
    
    class Meta:
        ordering = ['descricao']
    
    def __str__(self):
        return self.descricao
    
class UnidadeCapacidade(models.Model):
    '''Tabela que estabelece o relacionamento entre as unidades curriculares
    e as capacidades ou fundamentos técnicos e às capacidades Socioeconomica, 
    os dados são apenas as chaves estrangeiras das duas tabelas'''

    unidade = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    
class Pessoa(models.Model):
    COORDENADOR = 'Coordenador'
    ISTRUTOR = 'Instrutor'
    ASSISTENTE = 'Assistente'
    CARGO_CHOICE = [
        (COORDENADOR, 'Coordenador'),
        (ISTRUTOR, 'Instrutor'),
        (ASSISTENTE, 'Assistente')
    ]
    HORISTA = 'Horista'
    PRAZO_INDETER = 'Prazo Indeterminado'
    TEMPORARIO = 'Temporário'
    PRAZO_DETERMINADO = 'Prazo Determinado'
    VINCULO_CHOICES = [
        (HORISTA, 'Horista'),
        (PRAZO_INDETER, 'Prazo Indeterminado'),
        (TEMPORARIO, 'Temporário'),
        (PRAZO_DETERMINADO, 'Prazo Determinado')
    ]
    cargo = models.CharField(max_length = 20, choices=CARGO_CHOICE, default=ASSISTENTE )
    vinculo = models.CharField(max_length=20, choices=VINCULO_CHOICES, default=PRAZO_DETERMINADO)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    nif = models.CharField(max_length=20,  default = '00000')
    nivel = models.CharField(max_length=100, null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def disponivel_no_horario(self, data, horario_inicio, horario_fim):
        # Verificar se o professor já tem aula marcada nesse horário
        aulas_no_mesmo_horario = Aula.objects.filter(
            curso_uc_professor__professor=self,
            calendarioaula__dia_letivo__data=data,
            horario_inicio__lt=horario_fim,
            horario_fim__gt=horario_inicio
        )

        return not aulas_no_mesmo_horario.exists()


    class Meta:
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome


class HoratrabProf(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    horaEnter1 = models.TimeField()
    horaSaida1 = models.TimeField()
    horaEnter2 = models.TimeField(blank=True, null=True)  
    horaSaida2 = models.TimeField(blank=True, null=True)  
    data_inicio = models.DateField(default=datetime.date.today)
    data_fim = models.DateField(default=datetime.date.today)

    WEEKDAYS = [
        ("1", "Segunda"),
        ("Ter", "Terça"),
        ("Qua", "Quarta"),
        ("Qui", "Quinta"),
        ("Sex", "Sexta"),
        ("Sab", "Sábado"),
        ("Dom", "Domingo"),
    ]

    selected_days = ArrayField(
        models.CharField(max_length=3, choices=WEEKDAYS),
        default=list
    )

    quanthorames = models.IntegerField()

    def duracao_em_dias(self):
        return (self.data_fim - self.data_inicio).days

    def duracao_em_horas(self):
        # Convertendo TimeField para datetime para permitir a subtração
        duracao_delta1 = datetime.datetime.combine(datetime.date.today(), self.horaSaida1) - datetime.datetime.combine(datetime.date.today(), self.horaEnter1)
        if self.horaEnter2 and self.horaSaida2:
            duracao_delta2 = datetime.datetime.combine(datetime.date.today(), self.horaSaida2) - datetime.datetime.combine(datetime.date.today(), self.horaEnter2)
            total_delta = duracao_delta1 + duracao_delta2
        else:
            total_delta = duracao_delta1
        return total_delta.total_seconds() / 3600  # Convertendo para horas

    def turno(self):
        # Ajuste para usar os campos horaEnter1 e horaSaida2
        if self.horaEnter1 >= datetime.time(13, 0) and self.horaSaida2 <= datetime.time(22, 0):
            return "Tarde e Noite"
        elif self.horaEnter1 >= datetime.time(7, 30) and self.horaSaida1 <= datetime.time(17, 30):
            return "Manhã e Tarde"
        else:
            return "Noite"

    class Meta:
        ordering = ['pessoa']

    def __str__(self):
        # Ajuste para garantir que o método 'turno' e 'pessoa.nome' estejam corretos
        turno_str = self.turno() if self.horaEnter1 and self.horaSaida2 else "Indefinido"
        nome_pessoa = self.pessoa.nome if self.pessoa else "Pessoa Indefinida"
        return f"{nome_pessoa} - {turno_str} - {self.quanthorames} horas/mês"

class Areatecnologica(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    class Meta:
        ordering = ['nome']

    def __str__(self) -> str:
        return self.nome

class Infraestrutura(models.Model):
    TIPO_LABORATORIO = 'laboratorio'
    TIPO_OFICINA = 'oficina'
    TIPO_SALA_DE_AULA = 'sala_de_aula'
    # Outros tipos conforme necessário

    TIPO_AMBIENTE_CHOICES = [
        (TIPO_LABORATORIO, 'Laboratório'),
        (TIPO_OFICINA, 'Oficina'),
        (TIPO_SALA_DE_AULA, 'Sala de Aula'),
        # Outros tipos conforme necessário
    ]

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_AMBIENTE_CHOICES)
    capacidade = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()}) - Capacidade: {self.capacidade}"

class Curso(models.Model):
    APREND_IND = 'Aprendizagem industrial'
    TECNICO = 'Técnico'
    REGULAR_CHOICES = [
        (APREND_IND,'Aprendizagem industrial'),
        (TECNICO,'Técnico')
    ]
    INCIACAO = 'Iniciação'
    QUALIF = 'Qualificação'
    APERFEI = 'Aperfeiçoamento'
    ESPECIAL = 'Especialização'
    LIVRES_CHOICE = [
        (INCIACAO,'Iniciação'),
        (QUALIF,'Qualificação'),
        (APERFEI,'Aperfeiçoamento'),
        (ESPECIAL,'Especialização')
    ]
    curso_regular = models.CharField(max_length=30, choices=REGULAR_CHOICES, default = APREND_IND)
    curso_livre = models.CharField(max_length=30, choices=LIVRES_CHOICE, default = ESPECIAL)
    nome = models.CharField(max_length=100)
    quantidade_horas_total = models.IntegerField(blank=True, null=True)
    areatecnologica = models.ManyToManyField(Areatecnologica, blank=True)
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome



class Capacidades(models.Model):
    capacidadesSociais = models.TextField(blank=True)
    capacidadeTecnicaFundamentos = models.TextField(blank=True)
    unidadeCurricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.unidadeCurricular

class CursoUnidadeCurricularProfessor(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    unidadeCurricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, default = 1)

class CalendarioAcademico(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)  # Novo campo adicionado
    ano_letivo = models.IntegerField()
    semestre = models.IntegerField()
    inicio = models.DateField()
    termino = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Chama o save original primeiro
        self.create_or_update_dias_letivos()

    def create_or_update_dias_letivos(self):
        # Converta as datas de início e término para datetime.date, se ainda não forem
        start_date = self.inicio
        end_date = self.termino
        holidays = fetch_holidays(start_date.isoformat(), end_date.isoformat())

        current_date = start_date
        while current_date <= end_date:
            # Verifica se o dia é um feriado ou fim de semana
            e_dia_de_aula = not (current_date.weekday() in [5, 6] or current_date.isoformat() in holidays)

            # Cria ou atualiza o DiaLetivo
            DiaLetivo.objects.update_or_create(
                data=current_date,
                calendario_academico=self,
                defaults={'e_dia_de_aula': e_dia_de_aula}
            )

            # Incrementa a data atual
            current_date += timedelta(days=1)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.create_or_update_dias_letivos()

class DiaLetivo(models.Model):
    data = models.DateField()
    calendario_academico = models.ForeignKey(CalendarioAcademico, on_delete=models.CASCADE)
    e_dia_de_aula = models.BooleanField(default=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.data} - {'Aula' if self.e_dia_de_aula else 'Não-Aula'}"



class Aula(models.Model):
    curso_uc_professor = models.ForeignKey(CursoUnidadeCurricularProfessor, on_delete=models.CASCADE)

    def __str__(self):
        uc_nome = self.curso_uc_professor.unidadeCurricular.nome
        return f"Aula de {uc_nome}"

class AulaInfraestrutura(models.Model):
    aula = models.ForeignKey(Aula, related_name='aula_infraestruturas', on_delete=models.CASCADE)
    infraestrutura = models.ForeignKey(Infraestrutura, on_delete=models.CASCADE)
    horas = models.PositiveIntegerField()  # Armazena a quantidade de horas alocadas para essa infraestrutura em uma aula

    def __str__(self):
        return f"{self.aula} - {self.infraestrutura.nome} ({self.horas} horas)"




class CalendarioAula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    dia_letivo = models.ForeignKey(DiaLetivo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.aula} no dia {self.dia_letivo.data}"

    def clean(self):
        # Buscar aulas alocadas
        aulas_alocadas = Aula.objects.filter(
            curso_uc_professor__unidadeCurricular=self.aula.curso_uc_professor.unidadeCurricular
        ).filter(
            calendarioaula__isnull=False
        )
        # Verificação se a aula pode ser alocada neste dia letivo sem conflitos
        if not is_aula_disponivel_no_dia_letivo(self.aula, self.dia_letivo):
            raise ValidationError("Aula indisponível para este dia letivo.")

        # Verificação da disponibilidade da infraestrutura no horário da aula
        if not is_infraestrutura_disponivel(self.aula, self.aula.horario_inicio, self.aula.horario_fim):
            raise ValidationError("Infraestrutura indisponível no horário da aula.")

        # Verificação da disponibilidade do professor no horário da aula
        if not is_professor_disponivel(self.aula, self.aula.horario_inicio, self.aula.horario_fim):
            raise ValidationError("Professor não disponível no horário da aula.")

        # Verificação da carga horária da unidade curricular
        if not is_carga_horaria_respeitada(self.aula.curso_uc_professor.unidadeCurricular, self.aula, aulas_alocadas):
            raise ValidationError("A carga horária para esta unidade curricular já foi atingida ou excedida.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
