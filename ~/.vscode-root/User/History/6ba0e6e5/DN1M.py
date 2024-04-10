# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validar_data(value):
    '''Função que impede a data ser retroativa à data atual'''
    hoje = timezone.now().date()
    if value < hoje:
        raise ValidationError("A data não pode ser retroativa. Por favor selecione o dia atual ou uma data futura")

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    descricao_evento = models.CharField(max_length=100, blank=True, null=True)
    #data_evento = models.DateField(blank=True, null=True)
    data_evento = models.DateField(validators=[validar_data])
    class Meta:
        managed = False
        db_table = 'evento'

    def __str__(self):
        return self.descricao_evento

class Instituicao(models.Model):
    id_instituicao = models.AutoField(primary_key=True)
    codigo_instituicao = models.IntegerField(unique=True)
    nome_instiuicao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instituicao'

class Capacidade(models.Model):
    id_capacidade = models.AutoField(primary_key=True)
    descricao_capacidade = models.CharField(max_length=254, blank=True, null=True)
    tipo_capacidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'capacidade'

class Unidade(models.Model):
    id_unidade = models.AutoField(primary_key=True)
    descricao_unidade = models.CharField(max_length=254, blank=True, null=True)
    carga_horaria_total = models.IntegerField(blank=True, null=True)
    cor_capacidade = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidade'

class UnidadeCapacidade(models.Model):
    id_unidade_capacidade = models.AutoField(primary_key=True)
    id_unidade = models.ForeignKey(Unidade, models.DO_NOTHING, db_column='id_unidade')
    id_capacidade = models.ForeignKey(Capacidade, models.DO_NOTHING, db_column='id_capacidade')

    class Meta:
        managed = False
        db_table = 'unidade_capacidade'

class Periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    descricao_periodo = models.CharField(max_length=100, blank=True, null=True)
    turno_manha = models.IntegerField(blank=True, null=True)
    turno_tarde = models.IntegerField(blank=True, null=True)
    turno_noite = models.IntegerField(blank=True, null=True)
    dia_seg = models.IntegerField(blank=True, null=True)
    dia_ter = models.IntegerField(blank=True, null=True)
    dia_qua = models.IntegerField(blank=True, null=True)
    dia_qui = models.IntegerField(blank=True, null=True)
    dia_sex = models.IntegerField(blank=True, null=True)
    dia_sab = models.IntegerField(blank=True, null=True)
    dia_dom = models.IntegerField(blank=True, null=True)
    qtd_aula_dia = models.IntegerField(blank=True, null=True)
    qtd_dias_semana_aula = models.IntegerField(blank=True, null=True)
    tempo_aula_min = models.IntegerField(blank=True, null=True)
    hora_intervalo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'

class PeriodoDetalhe(models.Model):
    id_periodo_detalhe = models.AutoField(primary_key=True)
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo')
    tipo_periodo = models.IntegerField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fim = models.TimeField(blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo_detalhe'
        unique_together = (('id_periodo_detalhe', 'id_periodo'),)

class HoraIntervalo(models.Model):
    id_intervalo = models.AutoField(primary_key=True)
    hora_ini = models.TimeField(blank=True, null=True)
    hora_fim = models.TimeField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hora_intervalo'

class PeriodoIntervalo(models.Model):
    id_periodo_intervalo = models.AutoField(primary_key=True)
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo')
    id_intervalo = models.ForeignKey(HoraIntervalo, models.DO_NOTHING, db_column='id_intervalo')

    class Meta:
        managed = False
        db_table = 'periodo_intervalo'

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome_pessoa = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    tipo_pessoa = models.IntegerField(blank=True, null=True)
    vinculo = models.IntegerField(blank=True, null=True)
    cor_pessoa = models.CharField(max_length=10, blank=True, null=True)
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo')
    nif = models.FloatField(unique=True)

    class Meta:
        managed = False
        db_table = 'pessoa'

class AreaTecnologica(models.Model):
    id_area_tecnologica = models.AutoField(primary_key=True)
    descricao_area_tecnologica = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_tecnologica'

class Infraestrutura(models.Model):
    id_infraestrutura = models.AutoField(primary_key=True)
    descricao_infra = models.CharField(max_length=100, blank=True, null=True)
    tipo_infraestrutura = models.IntegerField(blank=True, null=True)
    cor_infraestrutura = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infraestrutura'

class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    descricao_turma = models.CharField(max_length=100, blank=True, null=True)
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo', blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    id_area_tecnologica = models.ForeignKey(AreaTecnologica, models.DO_NOTHING, db_column='id_area_tecnologica', blank=True, null=True)
    cor_turma = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turma'

class Aula(models.Model):
    id_aula = models.AutoField(primary_key=True)
    id_unidade = models.ForeignKey('Unidade', models.DO_NOTHING, db_column='id_unidade', blank=True, null=True)
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_turma', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aula'

class AulaSala(models.Model):
    id_aula_sala = models.AutoField(primary_key=True)
    id_aula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='id_aula')
    id_sala = models.ForeignKey('Infraestrutura', models.DO_NOTHING, db_column='id_sala')
    qtd_horas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aula_sala'

class AulaProfessor(models.Model):
    id_aula_professor = models.AutoField(primary_key=True)
    id_aula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='id_aula')
    id_pessoa = models.ForeignKey('Pessoa', models.DO_NOTHING, db_column='id_pessoa')

    class Meta:
        managed = False
        db_table = 'aula_professor'
