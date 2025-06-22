from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

def app_router(app, name): 
    for NAME in name: 
        app.mount("/" + NAME, StaticFiles(directory=NAME), name=NAME)

app = FastAPI(
    title="Mc Storage",
    description="Kho lưu trữ Mc's",
)
app_router(app, ["data", "image"])
