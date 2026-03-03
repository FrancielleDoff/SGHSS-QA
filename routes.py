from flask import Blueprint, request, jsonify
from models import db, Paciente, Medico, Agendamento
from services import validar_cpf, horario_disponivel

main = Blueprint("main", __name__)


# Cadastro de Paciente

@main.route("/cadastrar_paciente", methods=["POST"])
def cadastrar_paciente():
    dados = request.get_json()

    nome = dados.get("nome")
    cpf = dados.get("cpf")

    if not validar_cpf(cpf):
        return jsonify({"erro": "CPF inválido"}), 400

    novo = Paciente(nome=nome, cpf=cpf)
    db.session.add(novo)
    db.session.commit()

    return jsonify({"mensagem": "Paciente cadastrado com sucesso"}), 201



# Cadastro de Médico

@main.route("/cadastrar_medico", methods=["POST"])
def cadastrar_medico():
    dados = request.get_json()

    nome = dados.get("nome")
    especialidade = dados.get("especialidade")

    novo_medico = Medico(nome=nome, especialidade=especialidade)

    db.session.add(novo_medico)
    db.session.commit()

    return jsonify({"mensagem": "Médico cadastrado com sucesso"}), 201

# Agendamento de consultas

@main.route("/agendar_consulta", methods=["POST"])
def agendar_consulta():
    dados = request.get_json()

    horario = dados.get("horario")
    paciente_id = dados.get("paciente_id")
    medico_id = dados.get("medico_id")


    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return jsonify({"erro": "Paciente não encontrado"}), 404


    medico = Medico.query.get(medico_id)
    if not medico:
        return jsonify({"erro": "Médico não encontrado"}), 404


    if not horario_disponivel(horario, medico_id, Agendamento):
        return jsonify({"erro": "Horário indisponível"}), 400

    novo_agendamento = Agendamento(
        horario=horario,
        paciente_id=paciente_id,
        medico_id=medico_id
    )

    db.session.add(novo_agendamento)
    db.session.commit()

    return jsonify({"mensagem": "Consulta agendada com sucesso"}), 201