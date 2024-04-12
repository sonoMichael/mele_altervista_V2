from sqlalchemy import create_engine, text
import os
import base64


engine = create_engine(os.getenv("DB_CONNECTION_STRING"))

def load_description_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from description"))
        description = []
        for row in result.all():
            desc = row._asdict()
            desc['image'] = base64.b64encode(desc['image']).decode('utf-8')
            description.append(desc)
        return description
    
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

def load_projects_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from projects"))
        projects = []
        for row in result.all():
            project = row._asdict()
            project['image'] = base64.b64encode(project['image']).decode('utf-8')
            projects.append(project)
        return projects

def load_contacts_from_db():
    print("Inside function")
    with engine.connect() as conn:
        result = conn.execute(text("select * from contacts"))
        contacts = []
        for row in result.all():
            contact = row._asdict()
            contact['image'] = base64.b64encode(contact['image']).decode('utf-8')
            contacts.append(contact)
        return contacts