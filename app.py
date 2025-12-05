from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular_peso():

    peso = float(request.form["peso"])
    redondeo = 2

    masa = peso / 9.81

    pesos = {
        "mercurio": round(masa * 3.7, redondeo),
        "venus": round(masa * 8.87, redondeo),
        "tierra": round(peso, redondeo),
        "marte": round(masa * 3.72, redondeo),
        "jupiter": round(masa * 24.79, redondeo),
        "saturno": round(masa * 10.44, redondeo),
        "urano": round(masa * 8.69, redondeo),
        "neptuno": round(masa * 11.15, redondeo)
    }
    

    return render_template("mercurio.html", pesos=pesos)

@app.route("/templates/<nombre>.html", methods=["POST"])
def planeta(nombre):
    pesos = eval(request.form["pesos"])
    return render_template(f"{nombre}.html", pesos=pesos)

if __name__ == "__main__":
    app.run()
