from django.contrib import admin
from .models import (CapacidadesFundamentos,AulaInfraestrutura, Pessoa,  Periodo, Areatecnologica, Capacidades,
                     UnidadeCurricular, Infraestrutura, Curso, HoraAulaCargaHoraria, Evento, Aula, CadastroEscola)

# Registre aqui seus modelos
admin.site.register(Pessoa)
admin.site.register(Periodo)
admin.site.register(Areatecnologica)
admin.site.register(UnidadeCurricular)
admin.site.register(Infraestrutura)
admin.site.register(Curso)
#admin.site.register(CursoUnidadeCurricularProfessor)
#admin.site.register(CalendarioAcademico)
#admin.site.register(DiaLetivo)
admin.site.register(Evento)
admin.site.register(Aula)
#admin.site.register(CalendarioAula)
admin.site.register(AulaInfraestrutura)
admin.site.register(Capacidades)
admin.site.register(CadastroEscola)
admin.site.register(CapacidadesFundamentos)
admin.site.register(HoraAulaCargaHoraria)
