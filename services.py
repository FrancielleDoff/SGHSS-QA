def validar_cpf(cpf):

    #Valida se o CPF possui 11 dígitos numéricos.

    if not cpf:
        return False

    return len(cpf) == 11 and cpf.isdigit()


def horario_disponivel(horario, medico_id, Agendamento):

   # Verifica se o médico já possui consulta no horário informado.

    consulta_existente = Agendamento.query.filter_by(
        horario=horario,
        medico_id=medico_id
    ).first()

    return consulta_existente is None