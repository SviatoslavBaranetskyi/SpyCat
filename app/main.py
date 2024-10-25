from fastapi import FastAPI

from app.db.database import engine
from app.models import models
from app.routers.routers import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Spy Cat Agency!"}


app.include_router(router, prefix="/api")
