from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retreive_moods,
    retreive_mood_with_details, add_mood,
    
)
from app.server.models.when import (
    WhenSchema, FullReading, ResponseModel, ErrorResponseModel
    
)




router = APIRouter()

# Get all the Feelings/Moods witthout the readings
@router.get("/", response_description ="All Moods are retreived")
async def get_moods():
    moods = await retreive_moods()
    if moods:
        return  ResponseModel(moods, "All feelings/moods retreived successfully")
    return ResponseModel(moods, "Empty list returned")


# Get single mood/Feeling with readings
@router.get("/{id}", response_description="Single mood is retreived")       
async def get_one_with_details(id):
    one_mood  = await retreive_mood_with_details(id)
    if one_mood:
        return  ResponseModel( one_mood, "Single Reading received succesfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")


@router.post("/", response_description=" reading added successfully")
async def add_reading( readings: FullReading = Body(...)): 
    reading = jsonable_encoder(readings)
    new_reading = await add_mood(reading)
    return ResponseModel( new_reading, "Reading Added successfully")