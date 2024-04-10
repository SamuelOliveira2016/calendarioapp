from django.urls import path
from .views import ( alocar_aula_view, InfraestruturaAPIView, InfraestruturaDetailAPIView,  AulaAPIView, AulaInfraestruturaAPIView,
                    EventoAPIView, PeriodoAPIView, UnidadeCurricularAPIView ,PessoaAPIView, AreaTecnologicaAPIView,TurmaAPIView,
                    CadastroEscolaAPIView, CapacidadesFundamentosAPIView, HoraAulaCargaHorariaAPIView)

urlpatterns = [
    path('pessoas/', PessoaAPIView.as_view(), name='pessoas'),
    path('pessoas/<int:pk>/', PessoaAPIView.as_view()),  
    path('areastecnologicas/', AreaTecnologicaAPIView.as_view(), name='area_tecnologica'),
    path('turma/', TurmaAPIView.as_view(), name='turma'),
    path('unidadecurricular/', UnidadeCurricularAPIView.as_view(), name='unidadecurricular-list-create'),
    path('periodo/', PeriodoAPIView.as_view(), name='periodo-api'),
    path('eventos/', EventoAPIView.as_view(), name='eventos-list'),
    path('eventos/<int:pk>/', EventoAPIView.as_view(), name='evento-detail'),
    path('aulas/', AulaAPIView.as_view(), name='aula-list'),
    path('aula-infraestruturas/', AulaInfraestruturaAPIView.as_view(), name='aula-infraestrutura-list'),
    path('aulas/<int:pk>/', AulaAPIView.as_view(), name='aula-detail'),
    path('infraestruturas/', InfraestruturaAPIView.as_view(), name='infraestrutura-list'),
    path('infraestruturas/<int:pk>/', InfraestruturaDetailAPIView.as_view(), name='infraestrutura-detail'),
    path('alocar_aula/', alocar_aula_view, name='alocar_aula'),
    path('cadastro-escola/', CadastroEscolaAPIView.as_view(), name='cadastro'),
    path('capacidades-fundamentos/', CapacidadesFundamentosAPIView.as_view(), name='capacidade'),
    path('hora-aula-carga-horaria/', HoraAulaCargaHorariaAPIView.as_view(), name='horas')

]
