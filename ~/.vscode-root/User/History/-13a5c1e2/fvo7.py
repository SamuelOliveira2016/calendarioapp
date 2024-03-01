from rest_framework import serializers
from .models import (CapacidadesFundamentos, CadastroEscola, DiaLetivo, Infraestrutura,AulaInfraestrutura, CalendarioAula,
                     Aula, Evento, CalendarioAcademico, CursoUnidadeCurricularProfessor,
                     Pessoa, Curso, UnidadeCurricular, Areatecnologica,  Periodo)

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

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'
        
class DiaLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaLetivo
        fields = '__all__'

class AreaTecnologicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areatecnologica
        fields = ['id', 'nome', 'descricao']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    Periodo = PeriodoSerializer(read_only=True)

    class Meta:
        model = Pessoa
        fields = ['ativo','id','nome','telefone','email','cargo','vinculo','nif','nivel', 'Periodo']


class CursoUnidadeCurricularProfessorSerializer(serializers.ModelSerializer):
    curso_id = serializers.PrimaryKeyRelatedField(source='curso', queryset=Curso.objects.all(), write_only=True)
    unidadeCurricular_id = serializers.PrimaryKeyRelatedField(source='unidadeCurricular', queryset=UnidadeCurricular.objects.all(), write_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(source='professor', queryset=Pessoa.objects.all(), write_only=True)

    curso_detail = CursoSerializer(source='curso', read_only=True)
    unidadeCurricular_detail = UnidadeCurricularSerializer(source='unidadeCurricular', read_only=True)
    professor_detail = PessoaSerializer(source='pessoa', read_only=True)


    class Meta:
        model = CursoUnidadeCurricularProfessor
        fields = ['id', 'curso_id', 'unidadeCurricular_id', 'professor_id', 'curso_detail','unidadeCurricular_detail','professor_detail' ]  # Inclua todos os campos necessários




class UnidadeCurricularSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UnidadeCurricular
        fields = ['id', 'nome',  'curso']

class CalendarioAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioAcademico
        fields = '__all__'



class AulaInfraestruturaSerializer(serializers.ModelSerializer):
    infraestrutura = serializers.PrimaryKeyRelatedField(queryset=Infraestrutura.objects.all())
    aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all(), write_only=True)

    class Meta:
        model = AulaInfraestrutura
        fields = ['aula', 'infraestrutura', 'horas']

class AulaSerializer(serializers.ModelSerializer):
    curso_uc_professor = CursoUnidadeCurricularProfessorSerializer()
    aula_infraestruturas = AulaInfraestruturaSerializer(source='aula_infraestruturas_set', many=True, required=False)

    class Meta:
        model = Aula
        fields = '__all__'


class CalendarioAulaSerializer(serializers.ModelSerializer):
    aula = AulaSerializer()
    dia_letivo = DiaLetivoSerializer()

    class Meta:
        model = CalendarioAula
        fields = '__all__'

class InfraestruturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infraestrutura
        fields = '__all__'  # Inclui todos os campos do modelo
