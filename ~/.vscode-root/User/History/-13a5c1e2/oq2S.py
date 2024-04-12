from rest_framework import serializers
from .models import (Evento, Instituicao,Capacidade, Unidade, UnidadeCapacidade,
                     Periodo, PeriodoDetalhe, HoraIntervalo, PeriodoIntervalo, Pessoa, PessoaViagem, AreaTecnologica, Infraestrutura,Turma, Aula,
                     AulaSala, AulaProfessor)

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'data_evento', 'descricao']

class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = ['id', 'descricao', 'unidade']

class CapacidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacidade
        fields = ['id', 'descricao', 'tipo']

class UnidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidade
        fields = ['id','descricao','carga_horaria', 'capacidadeFundamentos','cor']

class UnidadeCapacidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeCapacidade
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class PeriodoDetalheSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoDetalhe
        fields = '__all__'

class HoraIntervaloSerialilzer(serializers.ModelSerializer):
    class Meta:
        model = HoraIntervalo
        fields = '__all__'

class PeriodoIntervaloSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoIntervalo
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    Periodo = PeriodoSerializer(read_only=True)

    class Meta:
        model = Pessoa
        fields = '__all__'

class PessoaViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaViagem
        fields = '__all__'

class AreaTecnologicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaTecnologica
        fields = ['id', 'descricao']

class InfraestruturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraestrutura
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'

class AulaSalaSerializer(serializers.ModelSerializer):
    aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all(), write_only=True)
    infraestrutura = serializers.PrimaryKeyRelatedField(queryset=Infraestrutura.objects.all())

    class Meta:
        model = AulaSala
        fields = ['aula', 'infraestrutura', 'horas']

class AulaprofessorSerializer(serializers.ModelSerializer):
    aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all())
    professor = serializers.PrimaryKeyRelatedField(queryset=Pessoa.objects.all())

    class Meta:
        model = AulaProfessor
        fields = ['aula', 'professor']