from django.contrib import admin
from .models import (Evento,CapacidadesFundamentos, CadastroEscola, UnidadeCurricular, UnidadeCapacidade, AulaInfraestrutura, Pessoa,  Periodo, Areatecnologica,  
                     Infraestrutura, Turma, HoraAulaCargaHoraria,  Aula)

# Modelos registrados
admin.site.register(Evento)
admin.site.register(CapacidadesFundamentos)
admin.site.register(CadastroEscola)
admin.site.register(UnidadeCurricular)
admin.site.register(UnidadeCapacidade)

admin.site.register(Pessoa)
admin.site.register(Periodo)
admin.site.register(Areatecnologica)
admin.site.register(Infraestrutura)
admin.site.register(Turma)
admin.site.register(Aula)
admin.site.register(AulaInfraestrutura)
admin.site.register(HoraAulaCargaHoraria)
