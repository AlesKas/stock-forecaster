import os

from fastapi import APIRouter

router = APIRouter()

@router.get('/idk2')
async def func():
    return {'hey' : os.getenv('API_URL')}