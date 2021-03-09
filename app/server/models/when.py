# These are the moods/the feelings
from datetime import datetime
from typing import  Optional, List
from pydantic import BaseModel, Field
from .bible import BibleVerse

class When(BaseModel):
    title: str = Field(..., title="Feelings", description="This is the mood or feeling or situation")
    description :str  = Field(None, description="Description of the mood or situation")
    
    

class FullReading(BaseModel):
    """This class is the Main Object containing the list of Bible Verses as suggested.
    """
    
    when: When = Field(...)
    readings: List[BibleVerse] = Field(...)
    
    class Config:
            title = 'Bible Verse(s) to read When...'
     
print(FullReading.schema_json(indent=2))