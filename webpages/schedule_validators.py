from .utilities import calcular_carga_horaria  # Importação da função



def is_aula_disponivel_no_dia_letivo(aula, dia_letivo):
    # Verifica se a aula já está alocada nesse dia letivo
    from .models import CalendarioAula  # Importação local

    aulas_no_dia = CalendarioAula.objects.filter(dia_letivo=dia_letivo)
    for aula_existente in aulas_no_dia:
        if aula_existente.aula == aula:
            return False
    return True

def is_infraestrutura_disponivel(aula, horario_inicio, horario_fim):
    from .models import Aula
    aulas_na_infraestrutura = Aula.objects.filter(infraestrutura=aula.infraestrutura)

    for aula_existente in aulas_na_infraestrutura:
        # Ignorar a própria aula que está sendo alocada
        if aula_existente.id == aula.id:
            continue

        if horario_inicio < aula_existente.horario_fim and horario_fim > aula_existente.horario_inicio:
            return False

    return True

def is_professor_disponivel(aula, horario_inicio, horario_fim):
    # Verifica se o professor está disponível no horário da aula
    from .models import   HoratrabProf
    horarios_professor = HoratrabProf.objects.filter(pessoa=aula.curso_uc_professor.professor.pessoa)
    for horario in horarios_professor:
        if horario_inicio >= horario.horatrabIni and horario_fim <= horario.horatrabFim:
            return True
    return False

def is_carga_horaria_respeitada(unidade_curricular, aula, aulas_alocadas):
    from .models import Aula, Infraestrutura, CalendarioAula
    if aulas_alocadas is None:
            aulas_alocadas = Aula.objects.filter(
                curso_uc_professor__unidadeCurricular=unidade_curricular
            ).filter(
                calendarioaula__isnull=False
            )
    # Calcula a carga horária da aula com base no tipo de infraestrutura
    #def calcular_carga_horaria(aula):
        #if aula.infraestrutura.tipo == Infraestrutura.TIPO_LABORATORIO:
           # return unidade_curricular.horas_laboratorio
        #elif aula.infraestrutura.tipo == Infraestrutura.TIPO_OFICINA:
            #return unidade_curricular.horas_oficina
        #elif aula.infraestrutura.tipo == Infraestrutura.TIPO_SALA_DE_AULA:
            #return unidade_curricular.horas_sala_aula
       # return 0
    #calcular_carga_horaria(aula)
    # Soma as cargas horárias das aulas já alocadas para a unidade curricular
    carga_horaria_atual = (sum(
    calcular_carga_horaria(a) for a in aulas_alocadas
    if a.curso_uc_professor.unidadeCurricular == unidade_curricular)//2
)
    print('carga_horaria_atual: ', carga_horaria_atual)



    print('Calculo carga horaria: ',(carga_horaria_atual))
    carga_horaria_necessaria = calcular_carga_horaria(aula)
    print(f"Carga horária atual para UC '{unidade_curricular.nome}': {carga_horaria_atual}")
    print(f"Carga horária necessária para a aula {aula.id}: {carga_horaria_necessaria}")
    print(f"Carga horária total permitida para UC: {unidade_curricular.carga_horaria}")
    print(carga_horaria_atual + carga_horaria_necessaria <= unidade_curricular.carga_horaria
)
    return carga_horaria_atual + carga_horaria_necessaria <= unidade_curricular.carga_horaria
