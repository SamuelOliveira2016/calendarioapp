from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from .aula_distributor import alocar_aulas
from django.views.decorators.csrf import csrf_exempt

from .models import (Evento,Instituicao,Capacidade,Unidade, UnidadeCapacidade,Periodo,
                     PeriodoDetalhe, HoraIntervalo, PeriodoIntervalo, Pessoa, AreaTecnologica, Infraestrutura, Turma, Aula, AulaSala,
                     AulaProfessor)
from .serializers import (EventoSerializer,InstituicaoSerializer,CapacidadeSerializer, 
                          UnidadeSerializer, UnidadeCapacidadeSerializer, PeriodoSerializer,
                          PeriodoDetalheSerializer, HoraIntervaloSerialilzer, PeriodoIntervaloSerializer, PessoaSerializer, AreaTecnologicaSerializer, 
                          InfraestruturaSerializer, TurmaSerializer, AulaSerializer, AulaSalaSerializer, 
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

class InstituicaoAPIView(APIView):
    '''APIview para cadastro de unidades que poderão utilizar a aplicação, operações CRUD completas'''

    def get(self, request):
        cadastro = Instituicao.objects.all()
        serializer = EventoSerializer(cadastro, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InstituicaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            cadastro = Instituicao.objects.get(pk=pk)
        except Instituicao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InstituicaoSerializer(cadastro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            cadastro = Instituicao.objects.get(pk=pk)
        except Instituicao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InstituicaoSerializer(cadastro, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            cadastro = Instituicao.objects.get(pk=pk)
        except Instituicao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        cadastro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CapacidadesAPIView(APIView):
    '''APIview para capacidades e fundamentos técnicos operações CRUD completas'''

    def get(self, request):
        capacidade = Capacidade.objects.all()
        serializer = CapacidadeSerializer(capacidade, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CapacidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            capacidade = Capacidade.objects.get(pk=pk)
        except Capacidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CapacidadeSerializer(capacidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            capacidade = Capacidade.objects.get(pk=pk)
        except Capacidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CapacidadeSerializer(capacidade, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            capacidade = Capacidade.objects.get(pk=pk)
        except Capacidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        capacidade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UnidadeAPIView(APIView):
    '''APIview para Unidade Curricular operações CRUD completas'''
    def get(self, request):
        unidades_curriculares = Unidade.objects.all()
        serializer = UnidadeSerializer(unidades_curriculares, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UnidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            unidade = Unidade.objects.get(pk=pk)
        except Unidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadeSerializer(unidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            unidade = Unidade.objects.get(pk=pk)
        except Unidade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UnidadeSerializer(unidade, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            unidade = Unidade.objects.get(pk=pk)
        except Unidade.DoesNotExist:
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
        except UnidadeCapacidade.DoesNotExist:
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

class PeriodoAPIView(APIView):
    '''APIView para períodos de aulas, dias e horários de trabalho com CRUD implementado'''
    # GET para listar todos os horários
    def get(self, request):
        periodo = Periodo.objects.all()
        serializer = PeriodoSerializer(periodo, many=True)
        return Response(serializer.data)

    # POST para criar um novo horário
    def post(self, request):
        serializer = PeriodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
            try:
                periodo = Periodo.objects.get(pk=pk)
            except Periodo.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = PeriodoSerializer(periodo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            periodo = Periodo.objects.get(pk=pk)
        except Periodo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        periodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PeriodoDetalheAPIView(APIView):
    '''APIView para definição dos horários geral com CRUD implementado'''
    # GET para listar todos os horários
    def get(self, request):
        periodo = PeriodoDetalhe.objects.all()
        serializer = PeriodoDetalheSerializer(periodo, many=True)
        return Response(serializer.data)

    # POST para criar um novo horário
    def post(self, request):
        serializer = PeriodoDetalheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
            try:
                periodo = PeriodoDetalhe.objects.get(pk=pk)
            except PeriodoDetalhe.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = PeriodoDetalheSerializer(periodo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            periodo = PeriodoDetalhe.objects.get(pk=pk)
        except PeriodoDetalhe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        periodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HoraIntervaloAPIView(APIView):
    '''APIView para definição dos intervalos geral com CRUD implementado'''
    # GET para listar todos os horários
    def get(self, request):
        periodo = HoraIntervalo.objects.all()
        serializer = HoraIntervaloSerialilzer(periodo, many=True)
        return Response(serializer.data)

    # POST para criar um novo horário
    def post(self, request):
        serializer = HoraIntervaloSerialilzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
            try:
                periodo = HoraIntervalo.objects.get(pk=pk)
            except HoraIntervalo.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = HoraIntervaloSerialilzer(periodo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            periodo = HoraIntervalo.objects.get(pk=pk)
        except HoraIntervalo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        periodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PeriodoIntervaloAPIView(APIView):
    '''APIView para definição dos intervalos geral com CRUD implementado'''
    # GET para listar todos os horários
    def get(self, request):
        periodo = PeriodoIntervalo.objects.all()
        serializer = PeriodoIntervaloSerializer(periodo, many=True)
        return Response(serializer.data)

    # POST para criar um novo horário
    def post(self, request):
        serializer = PeriodoIntervaloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
            try:
                periodo = PeriodoIntervalo.objects.get(pk=pk)
            except PeriodoIntervalo.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer = PeriodoIntervaloSerializer(periodo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            periodo = PeriodoIntervalo.objects.get(pk=pk)
        except PeriodoIntervalo.DoesNotExist:
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
        areas = AreaTecnologica.objects.all()
        serializer = AreaTecnologicaSerializer(areas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AreaTecnologicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        areaT = AreaTecnologica.objects.get(pk=pk)
        serializer = AreaTecnologicaSerializer(areaT, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        pessoa = get_object_or_404(AreaTecnologica, pk=pk)
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

class AulaSalaAPIView(APIView):
    '''APIView para agregação de aulas as suas respectivas infraestruturas'''
    def get(self, request):
        aula_infraestruturas = AulaSala.objects.all()
        serializer = AulaSalaSerializer(aula_infraestruturas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AulaSalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            aula_infraestrutura = AulaSala.objects.get(pk=pk)
        except AulaSala.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AulaSalaSerializer(aula_infraestrutura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            aula_infraestrutura = AulaSala.objects.get(pk=pk)
        except AulaSala.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AulaSalaSerializer(aula_infraestrutura, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            aula_infraestrutura = AulaSala.objects.get(pk=pk)
        except AulaSala.DoesNotExist:
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
