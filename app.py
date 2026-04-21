from flask import Flask
from models import db
from routes import main
from flask import render_template

#Criação da aplicação Flask
app = Flask(__name__, template_folder="templates", static_folder="static")

#configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sghss.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#inicialização do SQLAlchemy com a aplicação
db.init_app(app)

app.register_blueprint(main)

with app.app_context():
    db.create_all()
@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)