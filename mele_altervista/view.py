from flask import Flask, render_template
from mele_altervista import app
from database import *

home_btns = ["about", "projects", "contact"]

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