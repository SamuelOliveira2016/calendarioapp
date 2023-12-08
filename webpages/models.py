from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

class Vinculo(models.Model):
    HORISTA = 'horista'
    PRAZO_INDETER = 'prazo_indeter'
    TEMPORARIO = 'temporario'
    VINCULO_CHOICES = [
        (HORISTA, 'Horista'),
        (PRAZO_INDETER, 'Prazo Indeterminado'),
        (TEMPORARIO, 'Temporário'),
    ]
    
    horista = models.BooleanField(choices=VINCULO_CHOICES)
    prazo_indeter = models.BooleanField(choices=VINCULO_CHOICES)
    temporario = models.BooleanField(choices=VINCULO_CHOICES)
    prazoDeter = models.DateField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    horatrabProf = models.ForeignKey('HoratrabProf', on_delete=models.CASCADE)

class HoratrabProf(models.Model):
    horariotrabalho = models.TimeField()
    diastrabalho = models.IntegerField()
    quantmes = models.IntegerField()

class Professor(models.Model):
    nif = models.CharField(max_length=15, unique=True)
    cargonivel = models.CharField(max_length=255)
    listunidcurri = models.ManyToManyField('Planocurso')

class Areatecnologica(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

class Tipocurso(models.Model):
    CURSO_LIVRE = 'cursolivre'
    CURSO_REGULAR = 'cursoregular'
    CURSO_FIC = 'cursoFic'
    TIPOCURSO_CHOICES = [
        (CURSO_LIVRE, 'Curso Livre'),
        (CURSO_REGULAR, 'Curso Regular'),
        (CURSO_FIC, 'Curso FIC'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPOCURSO_CHOICES)

class Planocurso(models.Model):
    nomecurso = models.CharField(max_length=255)
    modulo = models.IntegerField()
    unidadecurricular = models.CharField(max_length=255)
    carcahorauc = models.IntegerField()
    competenciastecnicas = models.TextField()
    competenciasSOM = models.TextField()
    conhecimentos = models.TextField()
    areatecnologica = models.ForeignKey(Areatecnologica, on_delete=models.CASCADE)
    tipocurso = models.ForeignKey(Tipocurso, on_delete=models.CASCADE)

class Infra(models.Model):
    salaula = models.BooleanField(default=False)
    lab = models.BooleanField(default=False)
    oficina = models.BooleanField(default=False)
    capacid = models.IntegerField(blank=True, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    tipocurso = models.ForeignKey(Tipocurso, on_delete=models.CASCADE)

class Calendario(models.Model):
    MANHA = 'manhã'
    TARDE = 'tarde'
    NOITE = 'noite'
    PERIODO_CHOICES = [
        (MANHA, 'Manhã'),
        (TARDE, 'Tarde'),
        (NOITE, 'Noite'),
    ]
    
    diasLetivos = models.IntegerField()
    feriados = models.DateField(blank=True, null=True)
    pontes = models.DateField(blank=True, null=True)
    periodo = models.CharField(max_length=10, choices=PERIODO_CHOICES)
    infra = models.ForeignKey(Infra, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    tipocurso = models.ForeignKey(Tipocurso, on_delete=models.CASCADE)
