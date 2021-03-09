import motor.motor_asyncio as m_async
import os
from bson.objectid import ObjectId
from .models.when import FullReading, WhenSchema

# mongo_url = os.getenv(MONGODB_URL)
# Defined .env path
# env_path = Path(__file__).parent.parent / '.env'
# load_dotenv(verbose=True, dotenv_path=env_path)

MONGO_DETAILS = "mongodb://localhost:27017"

client = m_async.AsyncIOMotorClient(MONGO_DETAILS)
db = client.bibleVerses_db

when_Collection = db.get_collection("when_collection")
full_Collection = db.get_collection("full_reading_collection")

# helpers
def single_when_helper(when: WhenSchema ) -> dict:
    return {
        "id": str(when["_id"]),
        "title": when["title"],
         "description": when["description"],
    }

def full_reading_helper(reading :FullReading) -> dict:
    return {
        "id": str(reading["_id"]),
        "when": reading["when"],
        "readings": reading["readings"]
    }   


# CRUD Operations now

# Get all Moods/Situatons
async def retreive_moods():
    moods = []
    async for mood in when_Collection.find():
        moods.append(single_when_helper(mood))
    return moods

# Get all moods with  readings
async def retreive_moods_with_details(id: str) -> dict:
     mood = await full_Collection.find_one({"_id": ObjectId(id)})
     if  mood:
         return full_reading_helper(mood)
    
# Add mood to Database

async def add_mood( fullReading: FullReading) -> dict:
    readings = await  full_Collection.insert_one(fullReading)
    new_mood = await full_Collection.find_one({"_id": readings.inserted_id})
    return  full_reading_helper(new_mood)