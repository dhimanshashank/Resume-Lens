from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/api")
def hello_world():
    return {"message" : "Welcome to the Resume Lens"}