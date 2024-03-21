from fastapi import FastAPI

app = FastAPI()

@app.get("/mehdi")
def read_root():
    return "Hello World"