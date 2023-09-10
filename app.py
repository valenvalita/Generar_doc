from flask import Flask, render_template, request, redirect, jsonify
from utils.generar_doc import *

## http://localhost
app = Flask(__name__)

## http://localhost/
@app.route("/", methods=["GET",'POST'])
def landing_template():
    # Si el método es post
    if request.method=='POST':
        generar_doc()
        wordToPdf()
        return render_template("landing_template.html", mostrarPDF = True) 
    
    # Si el método es get 
    return render_template("landing_template.html", mostrarPDF = False)


## http://localhost/contrato_coliving
@app.route("/contrato_coliving", methods=["GET"])
def contrato_coliving():
    # Si el método es get 
    return render_template("contrato_coliving.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)