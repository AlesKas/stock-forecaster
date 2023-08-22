from fastapi import FastAPI

from routes.idk1 import router as router1
from routes.idk2 import router as router2


app = FastAPI()
app.include_router(router1)
app.include_router(router2)
