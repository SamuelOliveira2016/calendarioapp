from django.urls import path
from .views import ( EventoAPIView, CadastroEscolaAPIView, CapacidadesFundamentosAPIView, UnidadeCurricularAPIView, UnidadeCapacidadeAPIView,
                    PeriodoAPIView, HoraAulaCargaHorariaAPIView, PessoaAPIView, alocar_aula_view, InfraestruturaAPIView, InfraestruturaDetailAPIView,  AulaAPIView, AulaInfraestruturaAPIView,
                       AreaTecnologicaAPIView,TurmaAPIView,
                      )

urlpatterns = [
    path('eventos/', EventoAPIView.as_view(), name='eventos-list'),
    path('eventos/<int:pk>/', EventoAPIView.as_view(), name='evento-detail'),
    path('cadastro-escola/', CadastroEscolaAPIView.as_view(), name='cadastro'),
    path('capacidades-fundamentos/', CapacidadesFundamentosAPIView.as_view(), name='capacidade'),
    path('unidadecurricular/', UnidadeCurricularAPIView.as_view(), name='unidadecurricular-list-create'),
    path('unidade-capacidade/', UnidadeCapacidadeAPIView.as_view(), name='unidadeCapacidade'),
    path('periodo/', PeriodoAPIView.as_view(), name='periodo-api'),
    path('hora-aula-carga-horaria/', HoraAulaCargaHorariaAPIView.as_view(), name='horas'),
    path('pessoas/', PessoaAPIView.as_view(), name='pessoas'),
    path('pessoas/<int:pk>/', PessoaAPIView.as_view()),  
    
    path('areastecnologicas/', AreaTecnologicaAPIView.as_view(), name='area_tecnologica'),
    path('turma/', TurmaAPIView.as_view(), name='turma'),
    path('aulas/', AulaAPIView.as_view(), name='aula-list'),
    path('aula-infraestruturas/', AulaInfraestruturaAPIView.as_view(), name='aula-infraestrutura-list'),
    path('aulas/<int:pk>/', AulaAPIView.as_view(), name='aula-detail'),
    path('infraestruturas/', InfraestruturaAPIView.as_view(), name='infraestrutura-list'),
    path('infraestruturas/<int:pk>/', InfraestruturaDetailAPIView.as_view(), name='infraestrutura-detail'),
    path('alocar_aula/', alocar_aula_view, name='alocar_aula'),

]
