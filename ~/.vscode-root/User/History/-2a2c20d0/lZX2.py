from django.contrib import admin
from .models import (CapacidadesFundamentos,AulaInfraestrutura, Pessoa,  Periodo, Areatecnologica, Capacidades,
                     UnidadeCurricular, Infraestrutura, Turma, HoraAulaCargaHoraria, Evento, Aula, CadastroEscola)

# Modelos registrados
admin.site.register(Pessoa)
admin.site.register(Periodo)
admin.site.register(Areatecnologica)
admin.site.register(UnidadeCurricular)
admin.site.register(Infraestrutura)
admin.site.register(Turma)
admin.site.register(Evento)
admin.site.register(Aula)
admin.site.register(AulaInfraestrutura)
admin.site.register(Capacidades)
admin.site.register(CadastroEscola)
admin.site.register(CapacidadesFundamentos)
admin.site.register(HoraAulaCargaHoraria)
