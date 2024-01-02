from django.urls import path
from .views import alocar_aula_view, CursoUnidadeCurricularProfessorDetailAPIView, InfraestruturaAPIView ,InfraestruturaDetailAPIView, CalendarioAulaAPIView, AulaAPIView, EventoAPIView, CalendarioAcademicoAPIView , ProfessorDetailView,CursoUnidadeCurricularProfessorAPIView, ProfessorAPIView ,HoratrabProfAPIView, UnidadeCurricularAPIView ,PessoaAPIView, AreaTecnologicaAPIView, TipoCursoAPIView, CursoAPIView, VinculoAPIView

urlpatterns = [
    path('pessoas/', PessoaAPIView.as_view(), name='pessoas'),
    path('areastecnologicas/', AreaTecnologicaAPIView.as_view(), name='area_tecnologica'),
    path('tipocurso/', TipoCursoAPIView.as_view(), name='tipocurso-list-create'),
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('vinculos/', VinculoAPIView.as_view(), name='vinculos_api'),
    path('unidadecurricular/', UnidadeCurricularAPIView.as_view(), name='unidadecurricular-list-create'),
    path('horatrabprof/', HoratrabProfAPIView.as_view(), name='horatrabprof-api'),
    path('professores/', ProfessorAPIView.as_view(), name='professor-list'),
    path('curso-uc-professor/', CursoUnidadeCurricularProfessorAPIView.as_view(), name='curso-uc-professor-list'),
    path('curso-uc-professor/<int:curso_id>/', CursoUnidadeCurricularProfessorDetailAPIView.as_view(), name='curso-uc-professor-detail'),
    path('professor-details/<int:pk>/', ProfessorDetailView.as_view(), name='professor-detail'),
    path('calendario-academico/', CalendarioAcademicoAPIView.as_view(), name='calendario-academico-list'),
    path('calendario-academico/<int:pk>/', CalendarioAcademicoAPIView.as_view(), name='calendario-academico-detail'),
    path('eventos/', EventoAPIView.as_view(), name='eventos-list'),
    path('eventos/<int:pk>/', EventoAPIView.as_view(), name='evento-detail'),
    path('aulas/', AulaAPIView.as_view(), name='aula-list'),
    path('aulas/<int:pk>/', AulaAPIView.as_view(), name='aula-detail'),
    path('calendario_aulas/', CalendarioAulaAPIView.as_view(), name='calendario_aulas-list'),
    path('calendario_aulas/<int:pk>/', CalendarioAulaAPIView.as_view(), name='calendario_aula-detail'),
    path('infraestruturas/', InfraestruturaAPIView.as_view(), name='infraestrutura-list'),
    path('infraestruturas/<int:pk>/', InfraestruturaDetailAPIView.as_view(), name='infraestrutura-detail'),
    path('alocar_aula/', alocar_aula_view, name='alocar_aula'),

]
