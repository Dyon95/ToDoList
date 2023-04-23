from fastapi import FastApi
import models
from db import engine

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

app = FastApi()

#define endpoint
@app.get("/")
def home():
    return "HALLO"