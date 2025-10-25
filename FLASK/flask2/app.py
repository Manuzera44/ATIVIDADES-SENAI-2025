from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/produtos")
def listar_produtos():
    produtos = [

        {"nome": "Banana", "preço": 5, "estoque": 3},
        {"nome": "Feijão", "preço": 20, "estoque": 8},
        {"nome": "Coca Cola", "preço": 10, "estoque": 10},
        {"nome": "Corola", "preço": 70000, "estoque": 3},
        {"nome": "Pitaya", "preço": 8, "estoque": 1},
    ]
    
    return render_template("produtos.html", lista_produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)