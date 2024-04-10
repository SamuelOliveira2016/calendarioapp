from django.contrib import admin
from .models import (Evento,Capacidade, Instituicao, Unidade,
                     UnidadeCapacidade, Periodo, PeriodoDetalhe, HoraIntervalo, PeriodoIntervalo,
                     Pessoa, PessoaViagem, AreaTecnologica, Infraestrutura, Turma, Aula, AulaSala,
                     AulaProfessor)
                      

# Modelos registrados
admin.site.register(Evento)
admin.site.register(Capacidade)
admin.site.register(Instituicao)
admin.site.register(Unidade)
admin.site.register(UnidadeCapacidade)
admin.site.register(Periodo)
admin.site.register(PeriodoDetalhe)
admin.site.register(HoraIntervalo)
admin.site.register(PeriodoIntervalo)
admin.site.register(Pessoa)
admin.site.register(PessoaViagem)
admin.site.register(AreaTecnologica)
admin.site.register(Infraestrutura)
admin.site.register(Turma)
admin.site.register(Aula)
admin.site.register(AulaSala)
admin.site.register(AulaProfessor)
