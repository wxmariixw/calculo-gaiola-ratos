from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else: 
        altura = float(request.form.get("altura"))
        largura = float(request.form.get("largura"))
        profundidade = float(request.form.get("profundidade"))

        quantidaderatos = (altura * largura * profundidade) / 70792
        
        resultado = f'Cabem {quantidaderatos:.0f} ratinhos'
        
        return render_template("resultado.html", resultado=resultado)
        
        