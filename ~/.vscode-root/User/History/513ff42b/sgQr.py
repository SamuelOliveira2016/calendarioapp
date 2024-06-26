from django.urls import path
from .views import (DetalhesUnidadeCurricularAPIView, alocar_aula_view,
                    CursoUnidadeCurricularProfessorDetailAPIView, InfraestruturaAPIView,
                    InfraestruturaDetailAPIView, CalendarioAulaAPIView, AulaAPIView, AulaInfraestruturaAPIView,
                    EventoAPIView, CalendarioAcademicoAPIView , ProfessorDetailView,CursoUnidadeCurricularProfessorAPIView,
                    HoratrabProfAPIView, UnidadeCurricularAPIView ,PessoaAPIView, AreaTecnologicaAPIView,CursoAPIView,
                    CadastroEscolaAPIView, CapacidadesFundamentosAPIView)

urlpatterns = [
    path('pessoas/', PessoaAPIView.as_view(), name='pessoas'),
    path('pessoas/<int:pk>/', PessoaAPIView.as_view()),  
    path('areastecnologicas/', AreaTecnologicaAPIView.as_view(), name='area_tecnologica'),
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('unidadecurricular/', UnidadeCurricularAPIView.as_view(), name='unidadecurricular-list-create'),
    path('horatrabprof/', HoratrabProfAPIView.as_view(), name='horatrabprof-api'),
    path('curso-uc-professor/', CursoUnidadeCurricularProfessorAPIView.as_view(), name='curso-uc-professor-list'),
    path('curso-uc-professor/<int:curso_id>/', CursoUnidadeCurricularProfessorDetailAPIView.as_view(), name='curso-uc-professor-detail'),
    path('professor-details/<int:pk>/', ProfessorDetailView.as_view(), name='professor-detail'),
    path('calendario-academico/', CalendarioAcademicoAPIView.as_view(), name='calendario-academico-list'),
    path('calendario-academico/<int:pk>/', CalendarioAcademicoAPIView.as_view(), name='calendario-academico-detail'),
    path('eventos/', EventoAPIView.as_view(), name='eventos-list'),
    path('eventos/<int:pk>/', EventoAPIView.as_view(), name='evento-detail'),
    path('aulas/', AulaAPIView.as_view(), name='aula-list'),
    path('aula-infraestruturas/', AulaInfraestruturaAPIView.as_view(), name='aula-infraestrutura-list'),
    path('aulas/<int:pk>/', AulaAPIView.as_view(), name='aula-detail'),
    path('calendario_aulas/', CalendarioAulaAPIView.as_view(), name='calendario_aulas-list'),
    path('calendario_aulas/<int:pk>/', CalendarioAulaAPIView.as_view(), name='calendario_aula-detail'),
    path('infraestruturas/', InfraestruturaAPIView.as_view(), name='infraestrutura-list'),
    path('infraestruturas/<int:pk>/', InfraestruturaDetailAPIView.as_view(), name='infraestrutura-detail'),
    path('alocar_aula/', alocar_aula_view, name='alocar_aula'),
    path('unidadecurricular/detalhes/<int:pk>/', DetalhesUnidadeCurricularAPIView.as_view(), name='detalhes_unidade_curricular'),
    path('cadastro-escola/', CadastroEscolaAPIView.as_view(), name='cadastro'),
    path('capacidades-fundamentos/', CapacidadesFundamentosAPIView.as_view(), name='capacidade')
]
