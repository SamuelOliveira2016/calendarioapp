from django.urls import path
from .views import ProfessorAPIView ,HoratrabProfAPIView, UnidadeCurricularAPIView ,PessoaAPIView, AreaTecnologicaAPIView, TipoCursoAPIView, CursoAPIView, VinculoAPIView

urlpatterns = [
    path('pessoas/', PessoaAPIView.as_view(), name='pessoas'),
    path('areastecnologicas/', AreaTecnologicaAPIView.as_view(), name='area_tecnologica'),
    path('tipocurso/', TipoCursoAPIView.as_view(), name='tipocurso-list-create'),
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('vinculos/', VinculoAPIView.as_view(), name='vinculos_api'),
    path('unidadecurricular/', UnidadeCurricularAPIView.as_view(), name='unidadecurricular-list-create'),
    path('horatrabprof/', HoratrabProfAPIView.as_view(), name='horatrabprof-api'),
    path('professores/', ProfessorAPIView.as_view(), name='professor-list'),

]
