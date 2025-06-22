from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import os

def app_router(app, names): 
    for NAME in names: 
        if os.path.isdir(NAME):
            app.mount(f"/{NAME}", StaticFiles(directory=NAME), name=NAME)

app = FastAPI()
app_router(app, ["data", "image"])
