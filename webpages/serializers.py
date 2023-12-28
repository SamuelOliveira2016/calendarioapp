from rest_framework import serializers
from .models import CursoUnidadeCurricularProfessor,Tipocurso, Pessoa, Vinculo, Curso, UnidadeCurricular, Areatecnologica, Professor, HoratrabProf



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
        fields = ['id', 'horas_sala_aula','horas_laboratorio','horas_oficina','nome', 'capacidadeTecnicaFundamentos', 'capacidadesSociais', 'carga_horaria', 'curso']

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


    class Meta:
        model = CursoUnidadeCurricularProfessor
        fields = ['curso', 'unidadeCurricular', 'professor']

class UnidadeCurricularSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UnidadeCurricular
        fields = ['id', 'nome',  'curso']




    