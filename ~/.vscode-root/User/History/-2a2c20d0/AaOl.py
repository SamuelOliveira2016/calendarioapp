from django.contrib import admin
from .models import (Evento,CapacidadesFundamentos, CadastroEscola, UnidadeCurricular, UnidadeCapacidade, Periodo,
                     HoraAulaCargaHoraria, AulaInfraestrutura, Pessoa, Areatecnologica,  
                     Infraestrutura, Turma, Aula)

# Modelos registrados
admin.site.register(Evento)
admin.site.register(CapacidadesFundamentos)
admin.site.register(CadastroEscola)
admin.site.register(UnidadeCurricular)
admin.site.register(UnidadeCapacidade)
admin.site.register(Periodo)
admin.site.register(HoraAulaCargaHoraria)
admin.site.register(Pessoa)
admin.site.register(Areatecnologica)
admin.site.register(Infraestrutura)

admin.site.register(Turma)
admin.site.register(Aula)
admin.site.register(AulaInfraestrutura)
