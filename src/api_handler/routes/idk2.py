from fastapi import APIRouter

router = APIRouter()

@router.get('/idk2')
async def func():
    return {'hey' : 2}