from flask import Flask, render_template_string, redirect, request, url_for
import random

app = Flask(__name__)

contador = 0
sumador = 1
costo_mejora = 15

ESTILOS = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #65925f;
        padding: 2rem;
        text-align: center;
    }
    h1, h2 {
        color: #18cd69;
    }
    button, .boton {
        font-size: 1.2rem;
        padding: 0.7rem 1.5rem;
        margin: 1rem 0.5rem;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: transform 0.15s ease, background-color 0.3s ease;
        user-select: none;
    }
    button:hover, .boton:hover {
        background-color: #45a049;
        transform: scale(0.95);
    }
    button:active, .boton:active {
        transform: scale(0.9);
    }
    a {
        display: inline-block;
        margin-top: 1rem;
        color: #0050a5;
        text-decoration: none;
    }
    input {
        padding: 0.5rem;
        font-size: 1rem;
        border-radius: 5px;
        border: 1px solid #ff0000;
        margin: 0.5rem;
    }
</style>

<script>
// Sonido click base64 embebido
const clickSound = new Audio('data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YQgAAA==');

document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll("button, .boton");
    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            clickSound.currentTime = 0;
            clickSound.play();
        });
    });
});
</script>
"""

INDEX_HTML = ESTILOS + """
<!DOCTYPE html>
<html>
<head><title>Principal</title></head>
<body>
    <h1>Contador: {{ contador }}</h1>
    <h2>Mejora actual: +{{ sumador }} (Costo: {{ costo_mejora }})</h2>
    <form method="POST" action="/sumar"><button type="submit">Chambear</button></form>
    <form method="POST" action="/mejorarBoton"><button type="submit">Conseguir Un Ascenso</button></form>
    <a class="boton" href="/AdvinoTuNumero">Acudir A Un Chaman (Es al pedo pero bue)</a><br>
    <a class="boton" href="/loteria">ir a apostar</a>
</body>
</html>
"""

ADIVINADOR_HTML = ESTILOS + """
<!DOCTYPE html>
<html>
<head><title>Chaman</title></head>
<body>
    <h1>Chaman Adivinador de Números</h1>
    <form method="POST">
        <input type="number" name="numero" placeholder="Escribí un número" required>
        <br>
        <button type="submit">Enviar</button>
    </form>
    <a href="/">Volver al inicio</a>
</body>
</html>
"""

MOSTRAR_NUMERO_HTML = ESTILOS + """
<!DOCTYPE html>
<html>
<head><title>Tu Número</title></head>
<body>
    <h1>El número que ingresaste es: <strong>{{ numero }}</strong></h1>
    <a class="boton" href="/AdvinoTuNumero">Volver a Acudir</a><br>
    <a href="/">Volver al inicio</a>
</body>
</html>
"""

@app.route("/")
def principal():
    global contador, sumador, costo_mejora
    return render_template_string(INDEX_HTML, contador=contador, sumador=sumador, costo_mejora=costo_mejora)

@app.route("/sumar", methods=["POST"])
def sumar():
    global contador, sumador
    contador += sumador
    return redirect("/")

@app.route("/mejorarBoton", methods=["POST"])
def mejorar_boton():
    global contador, sumador, costo_mejora
    if contador >= costo_mejora:
        sumador += 1
        contador -= costo_mejora
        costo_mejora += 1
    return redirect("/")

@app.route("/AdvinoTuNumero", methods=["GET", "POST"])
def advino_tu_numero():
    if request.method == "POST":
        numero = request.form.get("numero")
        return redirect(url_for('mostrar_numero', numero=numero))
    return render_template_string(ADIVINADOR_HTML)

@app.route("/mostrarNumero")
def mostrar_numero():
    numero = request.args.get("numero")
    if not numero:
        return redirect(url_for('advino_tu_numero'))
    return render_template_string(MOSTRAR_NUMERO_HTML, numero=numero)

@app.route("/Nashe", methods=["GET", "POST"])
def nashe():
    if request.method == "POST":
        nombre = request.form.get("NoDefinedName")
        kg = request.form.get("NodefinedKG")
        return f"Nombre recibido: {nombre}, KG: {kg}"
    return render_template_string(ESTILOS + """
    <form method="POST">
        <input type="text" name="NoDefinedName" placeholder="Tu nombre" required>
        <input type="number" name="NodefinedKG" placeholder="KG" required> 
        <br><button type="submit">Enviar</button>
    </form>
    """)

@app.route("/messi")
def messi():
    texto = "Hola, tu nombre es: Pedro y "
    texto += "Pedro y " * 499
    texto += "Pedro."
    return texto

@app.route("/loteria")
def loteria():
    numdeloteria = random.randint(1, 100)
    numelegido = 20

    if (numdeloteria == numelegido):
        contador == contador + 100
        return "GANASTE 100 MONEDAS GG BROOO"
    return "Tengo " + str(contador) + " monedas."

if __name__ == "__main__":
    app.run(debug=True)