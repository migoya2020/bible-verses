from  typing import Optional
from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    bookNumber: int =Field(None, gt=0, lt=9)
    bookName: str = Field(...,)
    
class ChapterSchema(BaseModel):
     chapter: int = Field(..., gt=0)
     
class VerseSchema(BaseModel):
      verseStart: int = Field(..., gt=0)
      verseEnd: Optional[int] = Field(None, gt=0) #this will be shown if the value is available only
      
class Description(BaseModel):
      verseReading: str = Field("Not available yet", description='this is the actual bible reading', title="Verse")
      
      
class BibleVerse(BaseModel):
    """
    This is be a complete Bible Verse of your current Feelings/Moods/Situation
    """
    
    book: BookSchema = Field(...)
    chapter: ChapterSchema = Field(...)
    verse: VerseSchema = Field(...)
    
    
    
    class Config:
            title = 'Bible Verses'
            
# print(BibleVerse.schema_json(indent=2))