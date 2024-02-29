from django.contrib import admin
from .models import (CapacidadesFundamentos,AulaInfraestrutura, Pessoa,  HoratrabProf, Areatecnologica, Capacidades,
                     UnidadeCurricular, Infraestrutura, Curso, CursoUnidadeCurricularProfessor,
                     CalendarioAcademico, DiaLetivo, Evento, Aula, CalendarioAula, CadastroEscola)

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
admin.site.register(CadastroEscola)
admin.site.register(CapacidadesFundamentos)
