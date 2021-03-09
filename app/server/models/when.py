# These are the moods/the feelings
from datetime import datetime
from typing import  Optional, List
from pydantic import BaseModel, Field
from .bible import BibleVerse

class WhenSchema(BaseModel):
    title: str = Field(..., title="Feelings", description="This is the mood or feeling or situation")
    description :str  = Field(None, description="Description of the mood or situation")
    
    

class FullReading(BaseModel):
    """This class is the Main Object containing the list of Bible Verses as suggested.
    """
    
    when: WhenSchema = Field(...)
    readings: List[BibleVerse] = Field(...)
    
    class Config:
            title = 'Bible Verse(s) to read When...'
            schema_extra = {
                            "id": "6047986f6051d1ae912acb0a",
                            "when": {
                                "title": "Need Encouragement",
                                "description": "whenever you feel low and you want encouragement from anybody"
                            },
                            "readings": [
                                {
                                "book": {
                                    "bookNumber": 2,
                                    "bookName": "Corinthians"
                                },
                                "chapter": {
                                    "chapter": 1
                                },
                                "verse": {
                                    "verseStart": 3,
                                    "verseEnd": 4
                                },
                                "description": {
                                    "verseReadings": "3 Praise be to the God and Father of our Lord Jesus Christ, the Father of compassion and the God of all comfort, 4 who comforts us in all our troubles, so that we can comfort those in any trouble with the comfort we ourselves receive from God."
                                }
                                }
                            ]
                        }
   


# print(FullReading.schema_json(indent=2))

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}