from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

DATABASE_NAME = 'cityDB.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
base = declarative_base()
session = Session(engine)

def create_db():
    base.metadata.create_all(engine)