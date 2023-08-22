from fastapi import APIRouter

router = APIRouter()

@router.get('/idk1')
async def func():
    return {'hey' : 1}