from flask import Flask, render_template
from mele_altervista import app

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html",
                           name = "Michael Zhao")