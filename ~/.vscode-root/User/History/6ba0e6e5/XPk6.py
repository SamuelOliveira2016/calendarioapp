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
    data_evento = models.DateField(validators=[validar_data])

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
    capacidade = models.ForeignKey(CapacidadesFundamentos, on_delete=models.CASCADE, default=0)

class Periodo(models.Model):
    '''Cadastro dos possiveis períodos, quer estes sejam de professores,
    turmas, aulas ou calendários esse modelo é pai do modelo HoraAulaCargaHoraria'''
    descricao = models.CharField(max_length=100)
    PERIODO_CHOICE =[(1, 'manhã'),
                     (2, 'tarde'),
                     (3, 'noite')]
    
    periodo = ArrayField(models.IntegerField(choices=PERIODO_CHOICE), default=list)

    WEEKDAYS = [
        (1, "Segunda"),
        (2, "Terça"),
        (3, "Quarta"),
        (4, "Quinta"),
        (5, "Sexta"),
        (6, "Sábado"),
        (7, "Domingo"),
    ]
    diasSemana = ArrayField(models.IntegerField(choices=WEEKDAYS), default=list)

    aulasPorDia = models.IntegerField()
    diasAula = models.IntegerField()

    def __str__(self):
        return self.descricao
    
class HoraAulaCargaHoraria(models.Model):
    '''Modelo para especificação de horários e períodos, utiliza informações do modelo
    super Período'''
    descricao = models.CharField(max_length=100)
    periodo = models.OneToOneField(Periodo,on_delete= models.CASCADE)
    TIPO_CHOICE = [(1,'Aula'),
                   (2,'Intervalo'),
                   (3,'Viagem'),
                   (4,'Carga Horaria')]
    
    tipoRegistro = models.IntegerField(choices=TIPO_CHOICE)

    horaInicio = models.TimeField()
    horaFim = models.TimeField()
    dataInicio = models.DateField()
    dataFim = models.DateField()

class Pessoa(models.Model):
    '''Modelo que cria usuario do sistema, atribuindo o cargo, o vínculo, dados pessoais
     e se o mesmo está ativo para referenciar a disponibilidade de utilização'''
    CARGO_CHOICE = [
        (1, 'Coordenador'),
        (2, 'Instrutor'),
        (3, 'Assistente')
    ]
    
    VINCULO_CHOICES = [
        (1, 'Horista'),
        (2, 'Prazo Indeterminado'),
        (3, 'Temporário'),
        (4, 'Prazo Determinado')
    ]
    cargo = models.IntegerField(choices=CARGO_CHOICE)
    vinculo = models.IntegerField(choices=VINCULO_CHOICES)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    nif = models.IntegerField()
    nivel = models.CharField(max_length=10, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    cor = models.CharField(max_length=10, default='branco')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, default=1)

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

class Areatecnologica(models.Model):
    '''Modelo para relacionar as áreas técnológicas de estudos das Escolas,
    apenas a descrição é necessária'''
    descricao = models.CharField(max_length=255)

    class Meta:
        ordering = ['descricao']

    def __str__(self) -> str:
        return self.descricao

class Infraestrutura(models.Model):
    '''Modelo para selecionar infraestrutura são necessários os campos,
    nome, capacidade, cor e tipo (laboratório, sala de aula e oficina)'''
    TIPO_AMBIENTE_CHOICES = [
        (1, 'Laboratório'),
        (2, 'Oficina'),
        (3, 'Sala de Aula'),
    ]

    nome = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.IntegerField(choices=TIPO_AMBIENTE_CHOICES)
    capacidade = models.IntegerField(blank=True, null=True)
    cor = models.CharField(max_length=50)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()}) - Capacidade: {self.capacidade}"

class Turma(models.Model):
    '''Criação de turma para popular o calendario, os dados necessários são,
     descrição, datas de inicio e fim, cor e duas chaves estrangeiras NN uma para
     período e outra para área tecnológica'''
    
    descricao = models.CharField(max_length=255)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    areatecnologica = models.ManyToManyField(Areatecnologica, blank=True)
    periodo = models.ManyToManyField(Periodo)
    cor = models.CharField(max_length=10)
    class Meta:
        ordering = ['descricao']

    def __str__(self):
        return self.descricao

class Aula(models.Model):
    '''Tabela para configurar aula unitária de cada turma que ,todos os dados são chave estrageira
    é necessário ter os dados do professor, Unidade Curricular e Infraestrutura'''
    professor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    UnidadeCurricularF=models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    turma=models.ForeignKey(Turma,on_delete=models.CASCADE)
    infraestrutura=models.ForeignKey(Infraestrutura,on_delete=models.CASCADE)
    def __str__(self):
        uc_nome = self.turma
        return f"Aula de {uc_nome}"

class AulaInfraestrutura(models.Model):
    '''Tabela para a atribuição de aula a sua respectiva infraestrutura, para isso se faz necessário
    os dados da aula e da infraestrutura assim como a quantidade de horas selecionadas.'''
    aula = models.ForeignKey(Aula, related_name='aula_infraestruturas', on_delete=models.CASCADE)
    infraestrutura = models.ForeignKey(Infraestrutura, on_delete=models.CASCADE)
    horas = models.PositiveIntegerField()  # Armazena a quantidade de horas alocadas para essa infraestrutura em uma aula

    def __str__(self):
        return f"{self.aula} - {self.infraestrutura.nome} ({self.horas} horas)"

class AulaProfessor(models.Model):
    '''Tabela para atribuição de aula ao professor, para isso as duas chaves
    estrangeiras são necessárias'''
    aula=models.ForeignKey(Aula,on_delete=models.CASCADE)
    professor=models.ForeignKey(Pessoa,on_delete=models.CASCADE)

    def __str__(self):
        return f'Nome da aula: {self.aula}, nome do professor: {self.professor}'