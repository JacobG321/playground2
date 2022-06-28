
from tkinter import Y
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def play():
    multiplier = 3
    return render_template("index.html", multiplier=multiplier)


@app.route("/playnum/<int:multiplier>")
def playnum(multiplier):
    return render_template("index.html", multiplier=multiplier)

@app.route("/playnumcolor/<int:multiplier>/<string:color>")
def playnumcolor(multiplier, color):
    return render_template("index.html", multiplier=multiplier, color=color)





if __name__ == "__main__":
    app.run(debug=True)

