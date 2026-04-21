from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Define a tabela Paciente
class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)

    agendamentos = db.relationship("Agendamento", backref="paciente", lazy=True)

#define a tabela Medico
class Medico(db.Model):
    __tablename__ = "medicos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)

    agendamentos = db.relationship("Agendamento", backref="medico", lazy=True)

#Define a tabela Agendamento representa o agendamento de uma consulta
class Agendamento(db.Model):
    __tablename__ = "agendamentos"

    id = db.Column(db.Integer, primary_key=True)

    data = db.Column(db.String(10))
    horario = db.Column(db.String(10))

    paciente_id = db.Column(db.Integer, db.ForeignKey("pacientes.id"), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey("medicos.id"), nullable=False)