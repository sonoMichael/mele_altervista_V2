from flask import Flask, render_template
from mele_altervista import app

home_btns = ["profile", "projects", "contacts"]

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html",
                           name = "Michael",
                           num_btns = len(home_btns),
                           home_btns = home_btns)