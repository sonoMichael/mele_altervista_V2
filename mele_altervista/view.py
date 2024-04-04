from flask import Flask, render_template
from mele_altervista import app

home_btns = ["about", "projects", "contact"]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",
                           title = "Portfolio",
                           num_btns = len(home_btns),
                           home_btns = home_btns)