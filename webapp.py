from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder="./static")

@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/abogacia')
def abogacia():
    return render_template("abogacia.html")
@app.route('/mediacion')
def mediacion():
    return render_template("mediacion.html")


app.run()
