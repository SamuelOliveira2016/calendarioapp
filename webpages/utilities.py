#utilities.py


def calcular_carga_horaria(aula):
    from .models import Infraestrutura  # Importe quaisquer dependências necessárias

    # Implementação da função
    if aula.infraestrutura.tipo == Infraestrutura.TIPO_LABORATORIO:
        return aula.curso_uc_professor.unidadeCurricular.horas_laboratorio
    elif aula.infraestrutura.tipo == Infraestrutura.TIPO_OFICINA:
        return aula.curso_uc_professor.unidadeCurricular.horas_oficina
    elif aula.infraestrutura.tipo == Infraestrutura.TIPO_SALA_DE_AULA:
        return aula.curso_uc_professor.unidadeCurricular.horas_sala_aula
    return 0
