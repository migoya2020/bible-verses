from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retreive_moods,
    retreive_mood_with_details, add_mood, update_reading, remove_reading
    
)
from app.server.models.when import (
    WhenSchema, FullReading, ResponseModel, ErrorResponseModel
    
)




router = APIRouter()

# Get all the Feelings/Moods witthout the readings
@router.get("/", response_description ="All Moods are retreived")
async def get_readings():
    moods = await retreive_moods()
    if moods:
        return  ResponseModel(moods, "All feelings/moods retreived successfully")
    return ResponseModel(moods, "Empty list returned")


# Get single mood/Feeling with readings
@router.get("/{id}", response_description="Single mood is retreived")       
async def get_reading_details(id):
    one_mood  = await retreive_mood_with_details(id)
    if one_mood:
        return  ResponseModel( one_mood, "Single Reading received succesfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

# Post some reading data
@router.post("/", response_description=" reading added successfully")
async def add_reading( readings: FullReading = Body(...)): 
    reading = jsonable_encoder(readings)
    new_reading = await add_mood(reading)
    return ResponseModel( new_reading, "Reading Added successfully")

# Update reading
@router.put("/{id}")
async def update_reading_data(id:str, req: FullReading = Body(...)):
    req = {k: v for k, v in req.dict().items if  v  is not None}
    updated_reading =await update_reading( id, req )
    if updated_reading:
        return ResponseModel(
            
            "Reading with ID: {} was updated successfully".format(id),
            "Bible Reading  updated sucessfully"
            
        )
    return ErrorResponseModel(
        
        "Some Error occured", 404, "There has been an error updating the Bible reading"
    )
    
    
# Delete Reading
@router.delete("/{id}", response_description="Strudent Data Deleted from the Database")
async def delete_readng_data(id):
    deleted_reading = await remove_reading(id)
    if deleted_reading:
        return ResponseModel( "Data with ID: {}  deleted Successfully".format(id),
                              "Reading Deleted successfully"                
                             )
    return ErrorResponseModel( "There has been an error deleting the Reading", 404, "Reading  with ID: {0} Does not exist anymore".format(id))