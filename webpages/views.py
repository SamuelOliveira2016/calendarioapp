from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Professor, Vinculo ,Pessoa, Tipocurso, Areatecnologica, Curso, UnidadeCurricular, HoratrabProf
from .serializers import  ProfessorSerializer,UnidadeCurricularSerializer,VinculoSerializer, PessoaSerializer, TipoCursoSerializer, AreaTecnologicaSerializer, CursoSerializer, HoratrabProfSerializer

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

class TipoCursoAPIView(APIView):
    def get(self, request):
        tipos_curso = Tipocurso.objects.all()
        serializer = TipoCursoSerializer(tipos_curso, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TipoCursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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

class VinculoAPIView(APIView):
    def get(self, request):
        vinculos = Vinculo.objects.all()
        serializer = VinculoSerializer(vinculos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VinculoSerializer(data=request.data)
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

class ProfessorAPIView(APIView):
    def get(self, request):
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
