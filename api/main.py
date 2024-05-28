from fastapi import FastAPI

from api.endpoints.endpoints import router

app = FastAPI()

app.include_router(router)
