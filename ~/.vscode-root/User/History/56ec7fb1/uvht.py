from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from .aula_distributor import alocar_aulas
from django.views.decorators.csrf import csrf_exempt

from .models import (Evento,CadastroEscola,CapacidadesFundamentos,UnidadeCurricular, UnidadeCapacidade,PeriodoPai,
                     PeriodoFilha, Pessoa, Areatecnologica, Infraestrutura, Turma, Aula, AulaInfraestrutura,
                     AulaProfessor)
from .serializers import (EventoSerializer,CadastroEscolaSerializer,CapacidadesFundamentosSerializer, 
                          UnidadeCurricularSerializer, UnidadeCapacidadeSerializer, PeriodoPaiSerializer,
                          PeriodoFilhaSerializer, PessoaSerializer, AreaTecnologicaSerializer, 
                          InfraestruturaSerializer, TurmaSerializer, AulaSerializer, AulaInfraestruturaSerializer, 
                          AulaprofessorSerializer)

class EventoAPIView(APIView):
    '''APIview para Eventos, operações CRUD completas'''

    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventoSerializer(evento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventoSerializer(evento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CadastroEscolaAPIView(APIView):
    '''APIview para cadastro de unidades que poderão utilizar a aplicação, operações CRUD completas'''

    def get(self, request):
        cadastro = CadastroEscola.objects.all()
        serializer = EventoSerializer(cadastro, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CadastroEscolaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            cadastro = CadastroEscola.objects.get(pk=pk)
        except CadastroEscola.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CadastroEscolaSerializer(cadastro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            cadastro = CadastroEscola.objects.get(pk=pk)
        except CadastroEscola.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CadastroEscolaSerializer(cadastro, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            cadastro = CadastroEscola.objects.get(pk=pk)
        except CadastroEscola.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        cadastro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CapacidadesFundamentosAPIView(APIView):
    '''APIview para capacidades e fundamentos técnicos operações CRUD completas'''

    def get(self, request):
        capacidade = CapacidadesFundamentos.objects.all()
        serializer = CapacidadesFundamentosSerializer(capacidade, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CapacidadesFundamentosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            capacidade = CapacidadesFundamentos.objects.get(pk=pk)
        except CapacidadesFundamentos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CadastroEscolaSerializer(capacidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            capacidade = CapacidadesFundamentos.objects.get(pk=pk)
        except CapacidadesFundamentos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CapacidadesFundamentosSerializer(capacidade, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            capacidade = CapacidadesFundamentos.objects.get(pk=pk)
        except CapacidadesFundamentos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        capacidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnidadeCurricularAPIView(APIView):
    '''APIview para Unidade Curricular operações CRUD completas'''
    def get(self, request):
        unidades_curriculares = UnidadeCurricular.objects.all()
        serializer = UnidadeCurricularSerializer(unidades_curriculares, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UnidadeCurricularSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            unidade = UnidadeCurricular.objects.get(pk=pk)
        except UnidadeCurricular.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadeCurricularSerializer(unidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            unidade = UnidadeCurricular.objects.get(pk=pk)
        except UnidadeCurricular.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadeCurricularSerializer(unidade, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            unidade = UnidadeCurricular.objects.get(pk=pk)
        except UnidadeCurricular.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        unidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnidadeCapacidadeAPIView(APIView):
    '''APIview para Unidade e capacidade operações CRUD completas'''
    def get(self, request):
        unidadeCapacidade = UnidadeCapacidade.objects.all()
        serializer = UnidadeCapacidadeSerializer(unidadeCapacidade, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UnidadeCapacidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            unidadeC = UnidadeCapacidade.objects.get(pk=pk)
        except UnidadeCurricular.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadeCapacidadeSerializer(unidadeC, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            unidadeC = UnidadeCapacidade.objects.get(pk=pk)
        except UnidadeCapacidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadeCapacidadeSerializer(unidadeC, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            unidadeC = UnidadeCapacidade.objects.get(pk=pk)
        except UnidadeCapacidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        unidadeC.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PeriodoPaiAPIView(APIView):
    '''APIView para períodos de aulas, dias e horários de trabalho com CRUD implementado'''
    # GET para listar todos os horários
    def get(self, request):
        periodo = PeriodoPai.objects.all()
        serializer = PeriodoPaiSerializer(periodo, many=True)
        return Response(serializer.data)

    # POST para criar um novo horário
    def post(self, request):
        serializer = PeriodoPaiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
            try:
                periodo = PeriodoPai.objects.get(pk=pk)
            except PeriodoPai.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = PeriodoPaiSerializer(periodo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            periodo = PeriodoPai.objects.get(pk=pk)
        except PeriodoPai.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        periodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PeriodoFilhaAPIView(APIView):
    '''APIView para definição dos horários geral com CRUD implementado'''
    # GET para listar todos os horários
    def get(self, request):
        periodo = PeriodoFilha.objects.all()
        serializer = PeriodoFilhaSerializer(periodo, many=True)
        return Response(serializer.data)

    # POST para criar um novo horário
    def post(self, request):
        serializer = PeriodoFilhaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
            try:
                periodo = PeriodoFilha.objects.get(pk=pk)
            except PeriodoFilha.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = PeriodoFilhaSerializer(periodo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            periodo = PeriodoFilha.objects.get(pk=pk)
        except PeriodoFilha.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        periodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PessoaAPIView(APIView):
    '''APIview para realizar CRUD para a tabela pessoas'''
    def get(self, request):
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PessoaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk, format=None):
        pessoa = Pessoa.objects.get(pk=pk)
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AreaTecnologicaAPIView(APIView):
    '''APIView para setar áreas tecnológicas'''
    def get(self, request):
        areas = Areatecnologica.objects.all()
        serializer = AreaTecnologicaSerializer(areas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AreaTecnologicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        areaT = Areatecnologica.objects.get(pk=pk)
        serializer = AreaTecnologicaSerializer(areaT, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pessoa = get_object_or_404(Areatecnologica, pk=pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InfraestruturaAPIView(APIView):
    '''APIVIew para CRUD de infraestururas, retorna todos os dados'''
    # Método para listar todas as infraestruturas ou criar uma nova
    def get(self, request):
        infraestruturas = Infraestrutura.objects.all()
        serializer = InfraestruturaSerializer(infraestruturas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InfraestruturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        infra = Infraestrutura.objects.get(pk=pk)
        serializer = InfraestruturaSerializer(infra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        infra = get_object_or_404(Infraestrutura, pk=pk)
        infra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InfraestruturaDetailAPIView(APIView):
    '''APIVIew para CRUD de infraestururas, retorna apenas o objeto'''

    # Método auxiliar para obter uma infraestrutura pelo ID
    def get_object(self, pk):
        try:
            return Infraestrutura.objects.get(pk=pk)
        except Infraestrutura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # Método para obter detalhes de uma infraestrutura específica
    def get(self, request, pk):
        infraestrutura = self.get_object(pk)
        serializer = InfraestruturaSerializer(infraestrutura)
        return Response(serializer.data)

    # Método para atualizar uma infraestrutura
    def put(self, request, pk):
        infraestrutura = self.get_object(pk)
        serializer = InfraestruturaSerializer(infraestrutura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método para atualização parcial de uma infraestrutura
    def patch(self, request, pk):
        infraestrutura = self.get_object(pk)
        serializer = InfraestruturaSerializer(infraestrutura, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método para deletar uma infraestrutura
    def delete(self, request, pk):
        infraestrutura = self.get_object(pk)
        if infraestrutura is not None:
            infraestrutura.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class TurmaAPIView(APIView):
    '''APIView para configuração das turmas'''
    def get(self, request):
        Turmas = Turma.objects.all()
        serializer = TurmaSerializer(Turmas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TurmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk, format=None):
        turma = Turma.objects.get(pk=pk)
        serializer = TurmaSerializer(turma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pessoa = get_object_or_404(Turma, pk=pk)
        pessoa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AulaAPIView(APIView):
    '''APIView para a criação de aulas'''
    def get(self, request):
        aulas = Aula.objects.all()
        serializer = AulaSerializer(aulas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            aula = Aula.objects.get(pk=pk)
        except Aula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AulaSerializer(aula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            aula = Aula.objects.get(pk=pk)
        except Aula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AulaSerializer(aula, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            aula = Aula.objects.get(pk=pk)
        except Aula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        aula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AulaInfraestruturaAPIView(APIView):
    '''APIView para agregação de aulas as suas respectivas infraestruturas'''
    def get(self, request):
        aula_infraestruturas = AulaInfraestrutura.objects.all()
        serializer = AulaInfraestruturaSerializer(aula_infraestruturas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AulaInfraestruturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            aula_infraestrutura = AulaInfraestrutura.objects.get(pk=pk)
        except AulaInfraestrutura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AulaInfraestruturaSerializer(aula_infraestrutura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            aula_infraestrutura = AulaInfraestrutura.objects.get(pk=pk)
        except AulaInfraestrutura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AulaInfraestruturaSerializer(aula_infraestrutura, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            aula_infraestrutura = AulaInfraestrutura.objects.get(pk=pk)
        except AulaInfraestrutura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        aula_infraestrutura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AulaProfessorAPIView(APIView):
    '''APIView para agregação de aulas aos professores'''
    def get(self, request):
        aula_professor = AulaProfessor.objects.all()
        serializer = AulaprofessorSerializer(aula_professor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AulaprofessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            aula_professor = AulaProfessor.objects.get(pk=pk)
        except AulaprofessorSerializer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AulaprofessorSerializer(aula_professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            aula_professor = AulaProfessor.objects.get(pk=pk)
        except AulaProfessor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AulaprofessorSerializer(aula_professor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            aula_professor = AulaProfessor.objects.get(pk=pk)
        except AulaProfessor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        aula_professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt  # Remova isso se você estiver usando CSRF token na sua aplicação
def alocar_aula_view(request):
    if request.method == 'POST':
        # Lógica para lidar com requisições POST
        # Supondo que alocar_aulas() está sendo chamada corretamente
        alocar_aulas()
        return JsonResponse({"mensagem": "Aula alocada com sucesso"})

    else:
        # Se a requisição não for POST, retorna uma resposta indicando método não suportado
        return JsonResponse({"erro": "Método não suportado"}, status=405)
