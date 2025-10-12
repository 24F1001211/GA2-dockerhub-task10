from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"verification_number": 70577997}
