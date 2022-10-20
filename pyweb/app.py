from crypt import methods
from flask import Flask, render_template, request
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
    
@app.route("/conversao", methods=["POST","GET"])
def conversao():
    # (GET) é o caso quando usuario digita a url on browser
    if request.method == "GET":
       return render_template("conversao.html")
    else:
        #(POST) e quando envia o formulario (clica calcular)
        preco = float(request.form.get("preco"))
        # TODO: pegar o preço da cotacao em:
        # https://docs.awesomeapi.com.br/api-de-moedas
        valor_reais = preco * 5.24

        return render_template(
            "conversao.html", valor_reais = valor_reais)

@app.route("/imc", methods=["POST","GET"])
def calculaImc():
    if request.method == "GET":
         return render_template("imc.html")
    else:
        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        total = peso / (altura * altura)
        return render_template(
            "imc.html", total = total
        )


if __name__ == "__main__":
    app.run(debug=True)



