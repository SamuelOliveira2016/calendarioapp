from django.db import models
from django.contrib.postgres.fields import ArrayField

from datetime import datetime
from django.core.exceptions import ValidationError



class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nome

class Vinculo(models.Model):
    HORISTA = 'horista'
    PRAZO_INDETER = 'prazo_indeter'
    TEMPORARIO = 'temporario'
    PRAZO_DETERMINADO = 'prazo_determinado'
    VINCULO_CHOICES = [
        (HORISTA, 'Horista'),
        (PRAZO_INDETER, 'Prazo Indeterminado'),
        (TEMPORARIO, 'Temporário'),
        (PRAZO_DETERMINADO, 'prazo_determinado')
    ]
    vinculo = models.CharField(max_length=20, choices=VINCULO_CHOICES, default=PRAZO_DETERMINADO)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.pessoa.nome} - {self.get_tipo_vinculo_display()}"

class HoratrabProf(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    vinculo = models.ForeignKey(Vinculo, on_delete=models.CASCADE, null=True, blank=True)
    horatrabIni = models.TimeField()
    horatrabFim = models.TimeField()

    WEEKDAYS = [
        ("Seg", "Segunda"),
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

    def turno(self):
        if self.horatrabIni >= datetime.strptime("13:00", '%H:%M').time() and self.horatrabFim <= datetime.strptime("22:00", '%H:%M').time():
            return "Tarde e Noite"
        elif self.horatrabIni >= datetime.strptime("07:30", '%H:%M').time() and self.horatrabFim <= datetime.strptime("17:30", '%H:%M').time():
            return "Manhã e Tarde"
        else:
            return "Noite"

    def __str__(self):
        return f"{self.pessoa.nome} - {self.turno()} - {self.quanthorames} horas/mês"




class Areatecnologica(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome

class Tipocurso(models.Model):
    CURSO_LIVRE = 'cursolivre'
    CURSO_REGULAR = 'cursoregular'
    CURSO_FIC = 'cursoFic'
    TIPOCURSO_CHOICES = [
        (CURSO_LIVRE, 'Curso Livre'),
        (CURSO_REGULAR, 'Curso Regular'),
        (CURSO_FIC, 'Curso FIC'),
    ]
    
    nome_tipo_curso = models.CharField(max_length=20, choices=TIPOCURSO_CHOICES, unique=True)

    def __str__(self) -> str:
        return self.get_nome_tipo_curso_display()



class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    carga_horaria = models.IntegerField(blank=True, null=True)

    def __str__(self):
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

    nome = models.CharField(max_length=50, blank=True, null=True) # Ex.: 'Eletroeletrônica', 'Sala 01', etc.
    tipo = models.CharField(max_length=20, choices=TIPO_AMBIENTE_CHOICES)
    capacidade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()}) - Capacidade: {self.capacidade}"


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    quantidade_horas_total = models.IntegerField(blank=True, null=True)
    tipo_curso = models.ForeignKey(Tipocurso, on_delete=models.SET_NULL, null=True, blank=True)
    infraestruturas = models.ManyToManyField(Infraestrutura, blank=True)

    def __str__(self):
        return self.nome


    def __str__(self):
        return f"{self.curso.nome} - {self.unidade_curricular.nome}"

class Professor(Pessoa):
    nif = models.CharField(max_length=20, unique=True)
    nivel = models.CharField(max_length=100, null=True, blank=True)

    # Relação com Horário de Trabalho (opcional, dependendo da necessidade)
    horario_trabalho = models.ManyToManyField(HoratrabProf, blank=True)

    # Relação com Cursos que o Professor pode lecionar
    cursos = models.ManyToManyField(Curso, blank=True)

    def disponivel_no_horario(self, dia_letivo, horario):
        # Verificar se o professor tem um horário de trabalho que conflita
        # Isso pode exigir ajustes dependendo da estrutura do seu modelo HoratrabProf
        conflitos = self.horario_trabalho.filter(
            selected_days__contains=[dia_letivo.weekday()],
            horatrabIni__lte=horario,
            horatrabFim__gte=horario
        )
        return not conflitos.exists()

    def __str__(self):
        return f"{self.nome} - NIF: {self.nif} - Nível: {self.nivel}"

class CursoUnidadeCurricularProfessor(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    unidade_curricular = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE)
    professores = models.ManyToManyField(Professor)





class CalendarioAcademico(models.Model):
    ano_letivo = models.IntegerField()
    semestre = models.IntegerField()
    inicio = models.DateField()
    termino = models.DateField()

    def __str__(self):
        return f"Calendário {self.ano_letivo} - Semestre {self.semestre}"

class DiaLetivo(models.Model):
    data = models.DateField()
    calendario_academico = models.ForeignKey(CalendarioAcademico, on_delete=models.CASCADE)
    e_dia_de_aula = models.BooleanField(default=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.data} - {'Aula' if self.e_dia_de_aula else 'Não-Aula'}"

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.TextField()
    calendario_academico = models.ForeignKey(CalendarioAcademico, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.data}"


class Aula(models.Model):
    curso_uc_professor = models.ForeignKey(CursoUnidadeCurricularProfessor, on_delete=models.CASCADE)
    infraestrutura = models.ForeignKey(Infraestrutura, on_delete=models.CASCADE)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        uc_nome = self.curso_uc_professor.unidade_curricular.nome
        infra_nome = self.infraestrutura.get_tipo_display()
        return f"Aula de {uc_nome} em {infra_nome} ({self.horario_inicio}-{self.horario_fim})"

class CalendarioAula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    dia_letivo = models.ForeignKey(DiaLetivo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.aula} no dia {self.dia_letivo.data}"

    def clean(self):
        # Validação de sobreposição de horários para a mesma infraestrutura
        aulas_no_mesmo_dia_e_local = CalendarioAula.objects.filter(
            aula__infraestrutura=self.aula.infraestrutura,
            dia_letivo=self.dia_letivo
        ).exclude(id=self.id)

        for outra_aula in aulas_no_mesmo_dia_e_local:
            if (self.aula.horario_inicio < outra_aula.aula.horario_fim and
                self.aula.horario_fim > outra_aula.aula.horario_inicio):
                raise ValidationError("Conflito de horário na infraestrutura selecionada.")

        # Validação da disponibilidade do professor
        for professor in self.aula.curso_uc_professor.professores.all():
            if not professor.disponivel_no_horario(self.dia_letivo.data, self.aula.horario_inicio):
                raise ValidationError(f"O professor {professor.nome} não está disponível neste horário.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)