from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create new engine instance
engine = create_engine("sqlite:///todolist_api.db")

#create sessionmaker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()