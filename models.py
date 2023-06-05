import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Hero(Base):
    __tablename__ = 'hero'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=50), nullable=False)
    occipation = sq.Column(sq.String(length=500), nullable=False)
    gender = sq.Column(sq.String(length=10), nullable=False)

    def __str__(self):
        return f"ID:{self.id}; Name:{self.name}; \nOccupation:{self.occipation}; Gender:{self.gender};"


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)