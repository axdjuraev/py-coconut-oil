from fastapi import FastAPI
from src.presentation.api import v1


def register_routers(app: FastAPI):
    app.include_router(v1.auth_router, prefix='/api/v1/auth', tags=['Auth'])
    app.include_router(v1.tags_router, prefix='/api/v1/tags', tags=['Tags'])
    app.include_router(v1.binary_router, prefix='/api/v1/binary', tags=['Binary'])
    app.include_router(v1.obj_router, prefix='/api/v1/obj', tags=['Obj'])
