from flask import Flask, render_template
from datetime import datetime

#Flask é um framework web
#ele executa na porta 5000


#criado o servidor web(flask)
app = Flask(__name__)
# Flask é a classe
# app é a instancia(objeto)

#https://localhost:5000
@app.route("/")
def hello():
    agora = datetime.now()
    return f"<h1>Seja bem vindo - {agora}</h1>"

#https://localhost:5000/bomdia
@app.route("/bomdia")
def bomdia():
    return render_template("index.html")


@app.route("/cotacao")
def cotacao():
    valor = 5.21
    return render_template(
        "cotacao.html", valor = valor
        )



if __name__ == "__main__":
    app.run(debug=True)



