from flask import Flask, render_template
from mele_altervista import app

home_btns = ["about", "projects", "contact"]

profile_par = "BASTAAAAAAA"

jobs = [
    {
        "title": "t1",
        "period": "prx",
        "detail": "drx"
    },
    {
        "title": "t1 academy",
        "period": "psg",
        "detail": "dg"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",
                           title = "Portfolio",
                           num_btns = len(home_btns),
                           home_btns = home_btns)

@app.route("/about")
def about():
    return render_template("about.html",
                           desc = profile_par,
                           jobs = jobs)