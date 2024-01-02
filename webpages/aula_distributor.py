# aula_distributor.py
from .utilities import calcular_carga_horaria  # Importação da função

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

#def calcular_carga_horaria(aula):
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

    aulas_alocadas = [calendario_aula.aula for calendario_aula in CalendarioAula.objects.select_related('aula').all()]
    print(aulas_alocadas)
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

            # Convertendo horário de início e fim para objetos datetime
            data_arbitraria = datetime(2000, 1, 1)  # Data arbitrária
            inicio_dt = datetime.combine(data_arbitraria, horario_inicio)
            fim_dt = datetime.combine(data_arbitraria, horario_fim)

            # Calculando a duração da aula
            duracao_da_aula = (fim_dt - inicio_dt).total_seconds() / 3600
            print('conta duração aula: ',duracao_da_aula)

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

            if is_carga_horaria_respeitada(aula.curso_uc_professor.unidadeCurricular, aula, aulas_alocadas):
                print(f"    Carga horária respeitada para aula {aula.id}.")
            else:
                print(f"    Carga horária não respeitada para aula {aula.id}.")
            
            # Verifica se todas as condições para alocação da aula são satisfeitas
            
            if (is_aula_disponivel_no_dia_letivo(aula, dia) and
                is_infraestrutura_disponivel(aula, horario_inicio, horario_fim) and
                is_professor_disponivel(aula, horario_inicio, horario_fim) and
                is_carga_horaria_respeitada(aula.curso_uc_professor.unidadeCurricular, aula, aulas_alocadas)):
                

                calendario_aula = CalendarioAula(aula=aula, dia_letivo=dia)
                aulas_alocadas.append(calendario_aula.aula)  # Adiciona a aula atual à lista de aulas alocadas

                calendario_aula.save()
#                aulas_alocadas.append(calendario_aula.aula)  # Adiciona a aula atual à lista de aulas alocadas
                carga_horaria_alocada += duracao_da_aula
                print(f"Aula {aula.id} alocada no dia {dia.data}, carga horária alocada: {carga_horaria_alocada}")
                print('quantida aulas alocadas: ', carga_horaria_alocada)
                if carga_horaria_alocada >= carga_horaria_necessaria:
                    print('carga_horaria_alocada >= carga_horaria_necessaria: ', carga_horaria_alocada, carga_horaria_necessaria)
                    break  # Encerra a alocação se a carga horária necessária foi atendida

        if carga_horaria_alocada < carga_horaria_necessaria:
            print(f"Não foi possível alocar a carga horária total para a aula {aula.id}.")
