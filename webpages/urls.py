from django.urls import path
from .views import CalendarioAcademicoAPIView , ProfessorDetailView,CursoUnidadeCurricularProfessorAPIView, ProfessorAPIView ,HoratrabProfAPIView, UnidadeCurricularAPIView ,PessoaAPIView, AreaTecnologicaAPIView, TipoCursoAPIView, CursoAPIView, VinculoAPIView

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
    path('curso-uc-professor/<int:curso_id>/', CursoUnidadeCurricularProfessorAPIView.as_view(), name='curso-uc-professor-detail'),
    path('professor-details/<int:pk>/', ProfessorDetailView.as_view(), name='professor-detail'),
    path('calendario-academico/', CalendarioAcademicoAPIView.as_view(), name='calendario-academico-list'),
    path('calendario-academico/<int:pk>/', CalendarioAcademicoAPIView.as_view(), name='calendario-academico-detail'),

]
