# aula_distributor.py

from .schedule_validators import (
    is_aula_disponivel_no_dia_letivo,
    is_infraestrutura_disponivel,
    is_professor_disponivel,
    is_carga_horaria_respeitada
)
from datetime import datetime

def ordenar_aulas():
    from .models import Aula
    aulas = Aula.objects.all()
    aulas_ordenadas = sorted(
        aulas, 
        key=lambda a: a.curso_uc_professor.unidadeCurricular.carga_horaria,
        reverse=True
    )
    return aulas_ordenadas

def calcular_carga_horaria(aula):
    # Aqui você precisará implementar a lógica para calcular a carga horária da aula
    # com base na infraestrutura utilizada e na unidade curricular.
    # Por exemplo:
    uc = aula.curso_uc_professor.unidadeCurricular
    if aula.infraestrutura.tipo == 'laboratorio':
        return uc.horas_laboratorio
    elif aula.infraestrutura.tipo == 'oficina':
        return uc.horas_oficina
    elif aula.infraestrutura.tipo == 'sala_de_aula':
        return uc.horas_sala_aula
    return 0

def alocar_aulas():
    from .models import DiaLetivo, CalendarioAula, HoratrabProf
    aulas_ordenadas = ordenar_aulas()
    dias_letivos = DiaLetivo.objects.all()

    WEEKDAYS = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]

    for aula in aulas_ordenadas:
        carga_horaria_necessaria = calcular_carga_horaria(aula)
        carga_horaria_alocada = 0
        print(f"Processando aula {aula.id}, carga horária necessária: {carga_horaria_necessaria}")

        for dia in dias_letivos:
            if carga_horaria_alocada >= carga_horaria_necessaria:
                print(f"Carga horária necessária atingida para aula {aula.id}")
                break

            dia_da_semana = WEEKDAYS[dia.data.weekday()]
            professor = aula.curso_uc_professor.professor
            horario_inicio = aula.horario_inicio
            horario_fim = aula.horario_fim

            print(f"  Tentando alocar no dia {dia.data}, dia da semana: {dia_da_semana}, horário: {horario_inicio} - {horario_fim}")

            if is_aula_disponivel_no_dia_letivo(aula, dia):
                print(f"    Aula {aula.id} disponível neste dia letivo.")
            else:
                print(f"    Aula {aula.id} não disponível neste dia letivo.")
                continue

            if is_infraestrutura_disponivel(aula, horario_inicio, horario_fim):
                print(f"    Infraestrutura disponível para aula {aula.id}.")
            else:
                print(f"    Infraestrutura não disponível para aula {aula.id}.")
                continue

            if is_professor_disponivel(aula, horario_inicio, horario_fim):
                print(f"    Professor disponível para aula {aula.id}.")
            else:
                print(f"    Professor não disponível para aula {aula.id}.")
                continue

            if is_carga_horaria_respeitada(aula.curso_uc_professor.unidadeCurricular, aula):
                print(f"    Carga horária respeitada para aula {aula.id}.")
                calendario_aula = CalendarioAula(aula=aula, dia_letivo=dia)
                calendario_aula.save()
                carga_horaria_alocada += calcular_carga_horaria(aula)
                print(f"    Aula {aula.id} alocada no dia {dia.data}, carga horária alocada: {carga_horaria_alocada}")
            else:
                print(f"    Carga horária não respeitada para aula {aula.id}.")

        if carga_horaria_alocada < carga_horaria_necessaria:
            print(f"Não foi possível alocar a carga horária total para a aula {aula.id}.")
