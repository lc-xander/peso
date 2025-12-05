from flask import flask, render_template

app = flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

peso = float(request.form["peso"])

redondeo = 2

masa = peso / 9.81

pesoEnMercurio = round((masa * 3.7), redondeo)
pesoEnVenus = round((masa * 8.87), redondeo)
pesoEnTierra = round(peso, redondeo)
pesoEnMarte = round((masa * 3.72), redondeo)
pesoEnJupiter = round((masa * 24.79), redondeo)
pesoEnSaturno = round((masa * 10.44), redondeo)
pesoEnUrano = round((masa * 8.69), redondeo)
pesoEnNeptuno = round((masa * 11.15), redondeo)
