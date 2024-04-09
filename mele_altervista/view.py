from flask import Flask, render_template
from mele_altervista import app

home_btns = ["about", "projects", "contact"]

profile_par = "BASTAAAAAAA"

jobs = [
    {
        "title": "Barman",
        "period": "04/2023-08/2023",
        "detail": "Molino delle Armi"
    },
    {
        "title": "Waiter",
        "period": "06/2022-09/2022",
        "detail": "INARI Sushi Restaurant"
    }
]

pfp = ""

proj = [
    {
        "img": "../static/images/GBwHKo8akAAvcfP.jpg",
        "title": "Untitle",
        "detail": "Details",
        "url": ""
    }
]

cont = [
    {
        "img": "../static/images/mail.png",
        "title": "Personal mail",
        "url": "mailto:zhaomichael.business@gmail.com",
    },
    {
        "img": "../static/images/linkedin.png",
        "title": "Linkedin",
        "url": "https://www.linkedin.com/in/michael-zhao-60a50829b/"
    },
    {
        "img": "../static/images/github.png",
        "title": "Github",
        "url": "https://github.com/sonoMichael"
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