import os

from fastapi import FastAPI

from routes.stocks import router as stock_router
from routes.uploadFile import router as upload_file_router

app = FastAPI()
app.include_router(upload_file_router)
app.include_router(stock_router)