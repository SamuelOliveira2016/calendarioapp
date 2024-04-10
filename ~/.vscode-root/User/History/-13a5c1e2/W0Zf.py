from rest_framework import serializers
from .models import (Evento, CadastroEscola,CapacidadesFundamentos, UnidadeCurricular, UnidadeCapacidade,
                     Periodo, PeriodoDetalhe, Pessoa, Areatecnologica, Infraestrutura,Turma, Aula,
                     AulaInfraestrutura, AulaProfessor)

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'data_evento', 'descricao']

class CadastroEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroEscola
        fields = ['id', 'descricao', 'unidade']

class CapacidadesFundamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapacidadesFundamentos
        fields = ['id', 'descricao', 'tipo']

class UnidadeCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadeCurricular
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

class PessoaSerializer(serializers.ModelSerializer):
    Periodo = PeriodoSerializer(read_only=True)

    class Meta:
        model = Pessoa
        fields = ['ativo','id','nome','telefone','email','cargo','vinculo','nif','nivel', 'Periodo']

class AreaTecnologicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areatecnologica
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

class AulaInfraestruturaSerializer(serializers.ModelSerializer):
    aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all(), write_only=True)
    infraestrutura = serializers.PrimaryKeyRelatedField(queryset=Infraestrutura.objects.all())

    class Meta:
        model = AulaInfraestrutura
        fields = ['aula', 'infraestrutura', 'horas']

class AulaprofessorSerializer(serializers.ModelSerializer):
    aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all())
    professor = serializers.PrimaryKeyRelatedField(queryset=Pessoa.objects.all())

    class Meta:
        model = AulaProfessor
        fields = ['aula', 'professor']