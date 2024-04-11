from sqlalchemy import create_engine, Text
import os

engine = create_engine(os.getenv("DB_CONNECTION_STRING"),
                       connect_args={
                           "ssl": {
                               'sslmode': 'REQUIRED'
                           }
                       })

def load_description_from_db():
    with engine.connect() as conn:
        result = conn.execute(Text("select * from description"))
        description = []
        for row in result.all():
            description.append(dict(row))
        return description
    
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(Text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row))
        return jobs

def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(Text("select * from projects"))
        projects = []
        for row in result.all():
            projects.append(dict(row))
        return projects

def load_contacts_from_db():
    with engine.connect() as conn:
        result = conn.execute(Text("select * from contacts"))
        contacts = []
        for row in result.all():
            contacts.append(dict(row))
        return contacts
