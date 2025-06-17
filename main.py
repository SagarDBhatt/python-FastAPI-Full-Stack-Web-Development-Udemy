from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
#app = FastAPI()

@app.get("/")
def helloWorld():
    return {"message":"Hello, world"}