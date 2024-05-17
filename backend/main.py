from fastapi import FastAPI

from routes import auth

app = FastAPI()

app.include_router(auth.router)

