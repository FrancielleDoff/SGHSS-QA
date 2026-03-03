from flask import Flask
from models import db
from routes import main

#Criação da aplicação Flask
app = Flask(__name__)
#configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sghss.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#inicialização do SQLAlchemy com a aplicação
db.init_app(app)

app.register_blueprint(main)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)