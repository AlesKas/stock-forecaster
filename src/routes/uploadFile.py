import os

from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post('/uploadFile')
async def upload_file(file: UploadFile):
    file_location = f"./{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    if os.path.isfile(file_location):
        return JSONResponse(
            status_code=200,
            content={"message" : "File uploaded successfully"}
        )
    else:
        return JSONResponse(
            status_code=500,
            content={
                "message" : "There was an error while saving the file"
            }
        )