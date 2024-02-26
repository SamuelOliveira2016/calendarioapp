from django.contrib import admin
from .models import (AulaInfraestrutura, Pessoa,  HoratrabProf, Areatecnologica, Capacidades,
                     UnidadeCurricular, Infraestrutura, Curso, CursoUnidadeCurricularProfessor,
                     CalendarioAcademico, DiaLetivo, Evento, Aula, CalendarioAula)

# Registre aqui seus modelos
admin.site.register(Pessoa)
admin.site.register(HoratrabProf)
admin.site.register(Areatecnologica)
admin.site.register(UnidadeCurricular)
admin.site.register(Infraestrutura)
admin.site.register(Curso)
admin.site.register(CursoUnidadeCurricularProfessor)
admin.site.register(CalendarioAcademico)
admin.site.register(DiaLetivo)
admin.site.register(Evento)
admin.site.register(Aula)
admin.site.register(CalendarioAula)
admin.site.register(AulaInfraestrutura)
admin.site.register(Capacidades)
