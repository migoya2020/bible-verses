import motor.motor_asyncio as m_async
import os
from bson.objectid import ObjectId
from .models.when import FullReading

 
MONGO_DETAILS = "mongodb://localhost:27017"

client = m_async.AsyncIOMotorClient(MONGO_DETAILS)
db = client.bibleVerses_db

full_Collection = db.get_collection("full_reading_collection")

# helpers
def all_moods_helper(reading :FullReading ) -> dict:
    return {
        "id": str(reading["_id"]),
        "title": reading["when"]["title"],
         "description": reading["when"]["description"],
         "imageUrl":reading["when"]["imageUrl"],
    }

def reading_helper(reading :FullReading) -> dict:
    return {
        "id": str(reading["_id"]),
        "when": reading["when"],
        "readings": reading["readings"]
    }   


# CRUD Operations now

# Get all Moods/Situatons


async def retreive_moods():
    moods = []
    async for mood in full_Collection.find():
        moods.append(all_moods_helper(mood))
    return moods

# Get one Feeling with  reading details
async def retreive_mood_with_details(id: str) -> dict:
     mood = await full_Collection.find_one({"_id": ObjectId(id)})
     if  mood:
         return reading_helper(mood)
    
# Add mood/reading to Database
async def add_mood( fullReading: FullReading) -> dict:
    readings = await  full_Collection.insert_one(fullReading)
    new_mood = await full_Collection.find_one({"_id": readings.inserted_id})
    return  reading_helper(new_mood)

# Delete a reading
async def remove_reading(id:str):
    reading = await full_Collection.find_one({"_id": ObjectId(id)})
    if reading:
        await full_Collection.delete_one({"_id":ObjectId(id)})
        return True

#Update Reading
async def update_reading(id:str, data:dict):
    # return false if Body is Empty
    if len(data) <1:
        return False
    reading = await full_Collection.find_one({"_id": ObjectId})
    if reading:
        updated_reading = await full_Collection.update_one({"_id": ObjectId}, {"$set": data})
        if updated_reading:
            return True
        return False