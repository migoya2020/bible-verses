from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retreive_moods,
    retreive_moods_with_details,
    
)
from app.server.models.when import (
    When,
    
)




router = APIRouter()


@router.get("/", response_description ="All Moods are retreived")
async def get_moods ():
    moods = await retreive_moods()
    if moods:
        return When
    return "Error occured or Empty model"
        