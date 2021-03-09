import motor.motor_asyncio as m_async
import os
from bson.objectid import ObjectId

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
def single_when_helper(when) -> dict:
    return {
        "id": str(when["_id"]),
        "title": when["title"],
    }

def full_reading_helper(when) -> dict:
    return {
        "id": str(when["_id"]),
        "title": when["title"],
        "readings": when["readings"]
    }


# CRUD Operations now

# Get all Moods/Situatons
async def retreive_moods():
    moods = []
    async for mood in verse_Collection.find():
        moods.append(when_details_helper(mood))
    return moods

# Get all moods with  readings
async def retreive_moods_with_details():
    with_details = []
    async for mood in verse_Collection.find():
        with_details.append(when_details_helper(mood))
    return with_details