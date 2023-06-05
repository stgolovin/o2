import requests
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import Hero, create_tables


URL = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
LOGIN = 'postgres'
PASSWORD = 'MPuzo1920'
DB = 'o2_db'
DSN = f"postgresql://{LOGIN}:{PASSWORD}@db:5432/{DB}"

engine = sqlalchemy.create_engine(DSN, pool_pre_ping=True)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def save_data_from_api_to_db():
    r = requests.get(URL)
    data = r.json()
    for i in data:
        name = i['name']
        occipation = i['work']['occupation']
        gender = i['appearance']['gender']
        hero = Hero(name=name, occipation=occipation, gender=gender)
        session.add(hero)
        session.commit()


def watch_data_from_db():
    for i in session.query(Hero).all():
        print(i)


def main():
    save_data_from_api_to_db()
    watch_data_from_db()


if __name__ == "__main__":
    main()
