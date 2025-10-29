from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    titulo = "Holz's Collection"
    return render_template("index.html", titulo=titulo)

@app.route("/produtos")
def listar_produtos():
    produtos = [
        {"nome": "Bolacha", "preço": 3.90, "estoque": 9},
        {"nome": "Maça", "preço": 3.4, "estoque": 12},
        {"nome": "Leite", "preço": 7, "estoque": 3},
        {"nome": "Gol bolinha", "preço": 2190000, "estoque": 6},
        {"nome": "Banana", "preço": 10, "estoque": 1}
    ]
    return render_template("produtos.html", lista_produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)