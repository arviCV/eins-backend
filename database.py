from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "postgresql+psycopg2://postgres:RA701@localhost:5432/endpoint"

engine= create_engine(URL_DATABASE)

SessionLocal =sessionmaker(autocome=False, autoflush=False, bind=engine)

Base = declarative_base()