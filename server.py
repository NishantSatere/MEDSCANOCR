from fastapi import FastAPI
from routes.patient import router

app = FastAPI()

app.include_router(router)