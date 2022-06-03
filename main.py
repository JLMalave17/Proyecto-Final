from fastapi import FastAPI

from Router.usuario_router import router as user_router
from Router.libro_router import router as libro_router

app = FastAPI()

app.include_router(user_router)
app.include_router(libro_router)