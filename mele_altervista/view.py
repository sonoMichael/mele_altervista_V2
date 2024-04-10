from flask import Flask, render_template
from mele_altervista import app
from database import *

home_btns = ["about", "projects", "contact"]


description = [
    {
        "name": "",
        "surname": "",
        "photo": "",
        "summery": ""
    }
]

# jobs = [
#     {
#         "title": "Barman",
#         "period": "04/2023-08/2023",
#         "detail": "Molino delle Armi"
#     },
#     {
#         "title": "Waiter",
#         "period": "06/2022-09/2022",
#         "detail": "INARI Sushi Restaurant"
#     }
# ]

# proj = [
#     {
#         "img": "../static/images/projects/GBwHKo8akAAvcfP.jpg",
#         "title": "Untitle",
#         "detail": "Details",
#         "url": ""
#     }
# ]

# cont = [
#     {
#         "img": "../static/images/contacts/mail.png",
#         "title": "Personal mail",
#         "url": "mailto:zhaomichael.business@gmail.com",
#     },
#     {
#         "img": "../static/images/contacts/linkedin.png",
#         "title": "Linkedin",
#         "url": "https://www.linkedin.com/in/michael-zhao-60a50829b/"
#     },
#     {
#         "img": "../static/images/contacts/github.png",
#         "title": "Github",
#         "url": "https://github.com/sonoMichael"
#     }
# ]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",
                           title = "Portfolio",
                           num_btns = len(home_btns),
                           home_btns = home_btns)

@app.route("/about")
def about():
    description = load_description_from_db()
    jobs = load_jobs_from_db()
    return render_template("about.html",
                           title = "About",
                           description = description,
                           jobs = jobs)

@app.route("/projects")
def projects():
    projects = load_projects_from_db()
    return render_template("projects.html",
                           title = "Projects",
                           projects = projects)

@app.route("/contact")
def contact():
    contacts = load_contacts_from_db()
    return render_template("contact.html",
                           title = "Contact",
                           contacts = contacts)