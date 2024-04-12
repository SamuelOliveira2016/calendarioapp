from rest_framework import serializers
from .models import (Evento, CadastroEscola,CapacidadesFundamentos, UnidadeCurricular, UnidadeCapacidade,
                     Periodo, HoraAulaCargaHoraria, Pessoa, Areatecnologica, Infraestrutura,AulaInfraestrutura, 
                     Aula, Turma)

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

class HoraAulaCargaHorariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraAulaCargaHoraria
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




#class TurmaUnidadeCurricularProfessorSerializer(serializers.ModelSerializer):
#    Turma_id = serializers.PrimaryKeyRelatedField(source='Turma', queryset=Turma.objects.all(), write_only=True)
#    unidadeCurricular_id = serializers.PrimaryKeyRelatedField(source='unidadeCurricular', queryset=UnidadeCurricular.objects.all(), write_only=True)
#    professor_id = serializers.PrimaryKeyRelatedField(source='professor', queryset=Pessoa.objects.all(), write_only=True)
#
#    Turma_detail = TurmaSerializer(source='Turma', read_only=True)
#    unidadeCurricular_detail = UnidadeCurricularSerializer(source='unidadeCurricular', read_only=True)
#    professor_detail = PessoaSerializer(source='pessoa', read_only=True)
#
#
#    class Meta:
#        model = TurmaUnidadeCurricularProfessor
#        fields = ['id', 'Turma_id', 'unidadeCurricular_id', 'professor_id', 'Turma_detail','unidadeCurricular_detail','professor_detail' ]  # Inclua todos os campos necessários




class UnidadeCurricularSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UnidadeCurricular
        fields = ['id', 'nome',  'Turma']

#class CalendarioAcademicoSerializer(serializers.ModelSerializer):
#   class Meta:
#       model = CalendarioAcademico
#       fields = '__all__'



class AulaInfraestruturaSerializer(serializers.ModelSerializer):
    infraestrutura = serializers.PrimaryKeyRelatedField(queryset=Infraestrutura.objects.all())
    aula = serializers.PrimaryKeyRelatedField(queryset=Aula.objects.all(), write_only=True)

    class Meta:
        model = AulaInfraestrutura
        fields = ['aula', 'infraestrutura', 'horas']

class AulaSerializer(serializers.ModelSerializer):
    aula_infraestruturas = AulaInfraestruturaSerializer(source='aula_infraestruturas_set', many=True, required=False)

    class Meta:
        model = Aula
        fields = '__all__'


#class CalendarioAulaSerializer(serializers.ModelSerializer):
#    aula = AulaSerializer()
#    dia_letivo = DiaLetivoSerializer()
#
#    class Meta:
#        model = CalendarioAula
#        fields = '__all__'

