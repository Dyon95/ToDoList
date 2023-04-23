from fastapi import FastApi


app = FastApi()

#define endpoint
@app.get("/")
def home():
    return "HALLO"