from rest_framework import serializers
from .models import DiaLetivo, Infraestrutura, CalendarioAula, Aula, Evento, CalendarioAcademico, CursoUnidadeCurricularProfessor,Tipocurso, Pessoa, Vinculo, Curso, UnidadeCurricular, Areatecnologica, Professor, HoratrabProf

class DiaLetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaLetivo
        fields = '__all__'

class VinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinculo
        fields = ['id', 'pessoa','vinculo']

class TipoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipocurso
        fields = ['id', 'nome_tipo_curso']

class AreaTecnologicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areatecnologica
        fields = ['id', 'nome', 'descricao']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'quantidade_horas_total', 'tipo_curso']

class UnidadeCurricularSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnidadeCurricular
        fields = ['nome','id', 'horas_sala_aula','horas_laboratorio','horas_oficina','nome', 'capacidadeTecnicaFundamentos', 'capacidadesSociais', 'carga_horaria', 'curso']

class HoratrabProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoratrabProf
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    horatrabprof = HoratrabProfSerializer(read_only=True)

    class Meta:
        model = Pessoa
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField()
    pessoa = PessoaSerializer()


    class Meta:
        model = Professor
        fields = ['id', 'nif', 'nivel', 'pessoa', 'nome']

    def get_nome(self, obj):
        return obj.pessoa.nome


class CursoUnidadeCurricularProfessorSerializer(serializers.ModelSerializer):
    curso = CursoSerializer()
    unidadeCurricular = UnidadeCurricularSerializer()  # Incluir o serializer de Unidade Curricular
    professor = ProfessorSerializer()  # Incluir o serializer de Professor

    class Meta:
        model = CursoUnidadeCurricularProfessor
        fields = '__all__'  # Inclui todos os campos do modelo, incluindo o professor


class UnidadeCurricularSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UnidadeCurricular
        fields = ['id', 'nome',  'curso']

class CalendarioAcademicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioAcademico
        fields = ['id', 'aula','dia_letivo','nome','ano_letivo', 'semestre', 'inicio', 'termino']



class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nome', 'data_inicio', 'data_fim', 'descricao', 'calendario_academico']

class AulaSerializer(serializers.ModelSerializer):
    curso_uc_professor = CursoUnidadeCurricularProfessorSerializer()
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