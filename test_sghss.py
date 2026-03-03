#teste automatizado do sistema
import pytest
from app import app
from models import db

#utilização do pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()



# TESTE 1 - PACIENTE

def test_cadastro_paciente_valido(client):
    response = client.post("/cadastrar_paciente", json={
        "nome": "Maria",
        "cpf": "12345678909"
    })

    assert response.status_code == 201


def test_cadastro_paciente_cpf_invalido(client):
    response = client.post("/cadastrar_paciente", json={
        "nome": "João",
        "cpf": "000"
    })

    assert response.status_code == 400



# TESTE 2 - MÉDICO

def test_cadastro_medico(client):
    response = client.post("/cadastrar_medico", json={
        "nome": "Dr. Carlos",
        "especialidade": "Cardiologia"
    })

    assert response.status_code == 201



# TESTE 3 - AGENDAMENTO

def test_agendamento_valido(client):
    client.post("/cadastrar_paciente", json={
        "nome": "Maria",
        "cpf": "12345678909"
    })

    client.post("/cadastrar_medico", json={
        "nome": "Dr. Carlos",
        "especialidade": "Cardiologia"
    })

    from models import Paciente, Medico

    paciente = Paciente.query.first()
    medico = Medico.query.first()

    response = client.post("/agendar_consulta", json={
        "horario": "10:00",
        "paciente_id": paciente.id,
        "medico_id": medico.id
    })

    assert response.status_code == 201



# TESTE 4 - HORÁRIO OCUPADO

def test_horario_ja_ocupado(client):
    client.post("/cadastrar_paciente", json={
        "nome": "Maria",
        "cpf": "12345678909"
    })

    client.post("/cadastrar_medico", json={
        "nome": "Dr. Carlos",
        "especialidade": "Cardiologia"
    })

    from models import Paciente, Medico

    paciente = Paciente.query.first()
    medico = Medico.query.first()

    # Primeiro agendamento

    client.post("/agendar_consulta", json={
        "horario": "14:00",
        "paciente_id": paciente.id,
        "medico_id": medico.id
    })

    # Segundo no mesmo horário

    response = client.post("/agendar_consulta", json={
        "horario": "14:00",
        "paciente_id": paciente.id,
        "medico_id": medico.id
    })

    assert response.status_code == 400