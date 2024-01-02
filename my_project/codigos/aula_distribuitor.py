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
        print(f"Iniciando alocação para aula {aula.id}, carga horária necessária: {carga_horaria_necessaria}")

        for dia in dias_letivos:
            # Implementação da lógica de alocação
            if carga_horaria_alocada >= carga_horaria_necessaria:
                print(f"Carga horária necessária atingida para aula {aula.id}.")
                break  # Sair do loop se a carga horária necessária foi atingida

            print(f"Processando aula {aula.id} no dia {dia.data}")

            # Verificações de disponibilidade
            if (is_aula_disponivel_no_dia_letivo(aula, dia) and
                is_infraestrutura_disponivel(aula, aula.horario_inicio, aula.horario_fim) and
                is_professor_disponivel(aula, aula.horario_inicio, aula.horario_fim) and
                is_carga_horaria_respeitada(aula.curso_uc_professor.unidadeCurricular, aula)):

                calendario_aula = CalendarioAula(aula=aula, dia_letivo=dia)
                calendario_aula.save()
                carga_horaria_alocada += calcular_carga_horaria(aula)
                print(f"Aula {aula.id} alocada no dia {dia.data}, carga horária alocada: {carga_horaria_alocada}.")

        if carga_horaria_alocada < carga_horaria_necessaria:
            print(f"Não foi possível alocar a carga horária total para a aula {aula.id}.")

# Restante das funções de verificação (is_aula_disponivel_no_dia_letivo, etc.) ...
