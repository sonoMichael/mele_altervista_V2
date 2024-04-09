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

proj = [
    {
        "img": "../static/images/GBwHKo8akAAvcfP.jpg",
        "title": "title",
        "detail": "details"
    },
    {
        "img": "",
        "title": "title",
        "detail": "details"
    }
]

cont = [
    {
        "img": "../static/images/mail.png",
        "title": "Personal mail"
    },
    {
        "img": "../static/images/linkedin.png",
        "title": "Linkedin"
    },
    {
        "img": "../static/images/github.png",
        "title": "Github"
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
                           title = "About",
                           desc = profile_par,
                           jobs = jobs,
                           pfp = pfp)

@app.route("/projects")
def projects():
    return render_template("projects.html",
                           title = "Projects",
                           projects = proj)

@app.route("/contact")
def contact():
    return render_template("contact.html",
                           title = "Contact",
                           contacts = cont)