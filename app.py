from flask import Flask, render_template, abort
import json
app = Flask(__name__)

with open("MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/')
def inicio():
	return render_template("inicio.html")

app.run(debug=True)