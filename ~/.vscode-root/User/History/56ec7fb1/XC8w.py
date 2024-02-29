from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from .aula_distributor import alocar_aulas
from django.views.decorators.csrf import csrf_exempt

from .models import (AulaInfraestrutura, Infraestrutura, CalendarioAula,Aula,Evento,
                     CalendarioAcademico ,CursoUnidadeCurricularProfessor,Pessoa,
                     Areatecnologica, Curso, UnidadeCurricular, HoratrabProf)
from .serializers import (InfraestruturaSerializer, AulaInfraestruturaSerializer, CalendarioAulaSerializer,
                          AulaSerializer, EventoSerializer, CalendarioAcademicoSerializer,
                          UnidadeCurricularSerializer2 ,CursoUnidadeCurricularProfessorSerializer ,
                          UnidadeCurricularSerializer, PessoaSerializer,
                          AreaTecnologicaSerializer, CursoSerializer, HoratrabProfSerializer)

class PessoaAPIView(APIView):
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


class AreaTecnologicaAPIView(APIView):
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


class CursoAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UnidadeCurricularAPIView(APIView):
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

class DetalhesUnidadeCurricularAPIView(APIView):
    def get(self, request, pk):
        try:
            curso_uc_professor = CursoUnidadeCurricularProfessor.objects.get(pk=pk)
            unidade_curricular = curso_uc_professor.unidadeCurricular
            # Utilize o UnidadeCurricularSerializer para formatar a resposta ou crie uma resposta personalizada
            serializer = UnidadeCurricularSerializer(unidade_curricular)
            return Response(serializer.data)
        except CursoUnidadeCurricularProfessor.DoesNotExist:
            return Response({'error': 'CursoUnidadeCurricularProfessor não encontrado'}, status=status.HTTP_404_NOT_FOUND)


class HoratrabProfAPIView(APIView):
    # GET para listar todos os horários
    def get(self, request):
        horatrabprof = HoratrabProf.objects.all()
        serializer = HoratrabProfSerializer(horatrabprof, many=True)
        return Response(serializer.data)

    # POST para criar um novo horário
    def post(self, request):
        serializer = HoratrabProfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursoUnidadeCurricularProfessorAPIView(APIView):
    def get(self, request):
        cursos_uc_professor = CursoUnidadeCurricularProfessor.objects.all()
        serializer = CursoUnidadeCurricularProfessorSerializer(cursos_uc_professor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoUnidadeCurricularProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursoUnidadeCurricularProfessorDetailAPIView(APIView):
    def get_object(self, curso_id):
        try:
            return CursoUnidadeCurricularProfessor.objects.get(pk=curso_id)
        except CursoUnidadeCurricularProfessor.DoesNotExist:
            raise Http404

    def get(self, request, curso_id):
        curso_uc_professor = self.get_object(curso_id)
        serializer = CursoUnidadeCurricularProfessorSerializer(curso_uc_professor)
        return Response(serializer.data)

    def put(self, request, curso_id):
        curso_uc_professor = self.get_object(curso_id)
        serializer = CursoUnidadeCurricularProfessorSerializer(curso_uc_professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, curso_id):
        curso_uc_professor = self.get_object(curso_id)
        serializer = CursoUnidadeCurricularProfessorSerializer(curso_uc_professor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, curso_id):
        curso_uc_professor = self.get_object(curso_id)
        curso_uc_professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfessorDetailView(APIView):
    def get(self, request, pk):
        professor = Pessoa.objects.filter(pk=pk).select_related('nome').first()
        if not professor:
            return Response({"error": "Professor não encontrado"}, status=404)

        # Buscar as associações de CursoUnidadeCurricularProfessor para esse professor
        associacoes = CursoUnidadeCurricularProfessor.objects.filter(professor=professor)

        # Buscar registros HoratrabProf relacionados à Pessoa
        horatrabprof = HoratrabProf.objects.filter(pessoa=professor.pessoa)

        # Serializar os dados
        professor_data = ProfessorSerializer(professor).data
        associacoes_data = CursoUnidadeCurricularProfessorSerializer(associacoes, many=True).data
        horatrabprof_data = HoratrabProfSerializer(horatrabprof, many=True).data

        # Juntar os dados em uma única resposta
        response_data = {
            "professor": professor_data,
            "cursos_unidades_curriculares": associacoes_data,
            "horarios_trabalho": horatrabprof_data
        }

        return Response(response_data)
    
class CalendarioAcademicoAPIView(APIView):
    def get(self, request):
        calendarios = CalendarioAcademico.objects.all()
        serializer = CalendarioAcademicoSerializer(calendarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CalendarioAcademicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        calendario = get_object_or_404(CalendarioAcademico, pk=pk)
        serializer = CalendarioAcademicoSerializer(calendario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        calendario = get_object_or_404(CalendarioAcademico, pk=pk)
        calendario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EventoAPIView(APIView):
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

class AulaInfraestruturaAPIView(APIView):
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

    # PUT e PATCH podem ser implementados aqui se necessário
    # Deletar uma relação específica Aula-Infraestrutura
    def delete(self, request, pk):
        try:
            aula_infraestrutura = AulaInfraestrutura.objects.get(pk=pk)
        except AulaInfraestrutura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        aula_infraestrutura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AulaAPIView(APIView):
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
    
class CalendarioAulaAPIView(APIView):
    def get(self, request):
        calendario_aulas = CalendarioAula.objects.all()
        serializer = CalendarioAulaSerializer(calendario_aulas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CalendarioAulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            calendario_aula = CalendarioAula.objects.get(pk=pk)
        except CalendarioAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CalendarioAulaSerializer(calendario_aula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            calendario_aula = CalendarioAula.objects.get(pk=pk)
        except CalendarioAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CalendarioAulaSerializer(calendario_aula, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            calendario_aula = CalendarioAula.objects.get(pk=pk)
        except CalendarioAula.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        calendario_aula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class InfraestruturaAPIView(APIView):
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

class InfraestruturaDetailAPIView(APIView):

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
