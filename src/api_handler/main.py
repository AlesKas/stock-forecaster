import os

from fastapi import FastAPI

from routes.uploadFile import router as upload_file_router

app = FastAPI()
app.include_router(upload_file_router)
