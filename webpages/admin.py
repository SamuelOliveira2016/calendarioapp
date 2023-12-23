from django.contrib import admin
from .models import Pessoa, Vinculo, HoratrabProf, Areatecnologica, Tipocurso, UnidadeCurricular, Infraestrutura, Curso, Professor, CursoUnidadeCurricularProfessor, CalendarioAcademico, DiaLetivo, Evento, Aula, CalendarioAula

# Registre aqui seus modelos
admin.site.register(Pessoa)
admin.site.register(Vinculo)
admin.site.register(HoratrabProf)
admin.site.register(Areatecnologica)
admin.site.register(Tipocurso)
admin.site.register(UnidadeCurricular)
admin.site.register(Infraestrutura)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(CursoUnidadeCurricularProfessor)
admin.site.register(CalendarioAcademico)
admin.site.register(DiaLetivo)
admin.site.register(Evento)
admin.site.register(Aula)
admin.site.register(CalendarioAula)
