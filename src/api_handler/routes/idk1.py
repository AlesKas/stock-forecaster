import os

from fastapi import APIRouter

router = APIRouter()

@router.get('/idk1')
async def func():
    return {'hey' : os.getenv('API_KEY')}