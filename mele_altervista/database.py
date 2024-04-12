from sqlalchemy import create_engine, text
import os
from PIL import Image
import io


engine = create_engine(os.getenv("DB_CONNECTION_STRING"))

try:
    def load_description_from_db():
        with engine.connect() as conn:
            print("CONNECTED")
            result = conn.execute(text("select * from description"))
            description = []
            for row in result.all():
                description.append(row._mapping)
            return description
        
    def load_jobs_from_db():
        with engine.connect() as conn:
            result = conn.execute(text("select * from jobs"))
            jobs = []
            for row in result.all():
                jobs.append(row._mapping)
            return jobs

    def load_projects_from_db():
        with engine.connect() as conn:
            result = conn.execute(text("select * from projects"))
            projects = []
            for row in result.all():
                projects.append(row._mapping)
            return projects

    def load_contacts_from_db():
        print("Inside function")
        with engine.connect() as conn:
            result = conn.execute(text("select * from contacts"))
            print("Initialize result")
            contacts = []
            for row in result.all():
                contacts.append(row._mapping)
                # contacts[row]['image'] = Image.open(io.BytesIO(row['image']))
            return contacts
except:
    print("ERRORE")