from fastapi import FastAPI
from app.routers import router
from app.initializers import dir

app = FastAPI()

app.include_router(router)

# initializers
dir.set_working_directory()
