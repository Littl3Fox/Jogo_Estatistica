from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "qualquercoisa"
app.permanent_session_lifetime = timedelta(minutes=10)

# CONFIGURA TEMPO POR CLASSE
TEMPOS = {
    "guerreiro": 90,
    "berserk": 60,
    "mago": 120
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/iniciar", methods=["POST"])
def iniciar():
    classe = request.form.get("classe")


    session["classe"] = classe
    session["pontos"] = 0

    return redirect(url_for("cena1"))

@app.route("/cena1")
def cena1():
    tempo = TEMPOS[session["classe"]]
    return render_template("cena1.html", tempo=tempo)

@app.route("/cena2")
def cena2():
    tempo = TEMPOS[session["classe"]]
    return render_template("cena2.html", tempo=tempo)

@app.route("/cena3")
def cena3():
    tempo = TEMPOS[session["classe"]]
    return render_template("cena3.html", tempo=tempo)

@app.route("/fim")
def fim():
    pontos = session.get("pontos", 0)
    nome = session.get("nome", "")
    return render_template("fim.html", pontos=pontos, nome=nome)

@app.route("/add_ponto", methods=["POST"])
def add_ponto():
    session["pontos"] += int(request.form.get("valor"))
    proxima = request.form.get("proxima")
    return redirect(url_for(proxima))

@app.route("/penalidade", methods=["POST"])
def penalidade():
    session["pontos"] -= 10   # desconta 10 pontos
    proxima = request.form.get("proxima")
    return redirect(url_for(proxima))


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
