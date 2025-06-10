from fastapi import FastAPI

from auth import resources as auth_resources


def get_version():
    return '0.1.0'

app = FastAPI(
    title="Codsworth2",
    version=get_version(),
)

app.include_router(auth_resources.router)
