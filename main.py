from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from AWS EC2!",
        "status": "running",
        "platform": "Docker + FastAPI"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
