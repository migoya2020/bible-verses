from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retreive_moods,
    retreive_moods_with_details, add_mood,
    
)
from app.server.models.when import (
    WhenSchema, FullReading, ResponseModel
    
)




router = APIRouter()


@router.get("/", response_description ="All Moods are retreived")
async def get_moods ():
    moods = await retreive_moods()
    if moods:
        return WhenSchema
    return "Error occured or Empty model"



@router.get("/{id}", response_description="Single mood is retreived")       
async def get_one_with_details(id):
    one_mood  = await retreive_moods_with_details(id)
    if one_mood:
        return  FullReading( one_mood, "Single Data received succesfully")
    return "404 Error occured"

@router.post("/", response_description=" reading added successfully")
async def add_reading( readings: FullReading = Body(...)): 
    reading = jsonable_encoder(readings)
    new_reading = await add_mood(reading)
    return ResponseModel( new_reading, "Reading Added successfully")