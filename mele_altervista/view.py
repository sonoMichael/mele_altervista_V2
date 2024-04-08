from flask import Flask, render_template
from mele_altervista import app

home_btns = ["about", "projects", "contact"]

profile_par = "BASTAAAAAAA"

jobs = [
    {
        "title": "t1",
        "period": "2018-2020",
        "detail": "drx"
    },
    {
        "title": "t1 academy",
        "period": "2017-2018",
        "detail": "dg"
    }
]

pfp = ""

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
                           title = "About",
                           desc = profile_par,
                           jobs = jobs,
                           pfp = pfp)

@app.route("/projects")
def projects():
    pass

@app.route("/contact")
def contact():
    pass