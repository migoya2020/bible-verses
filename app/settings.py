from pydantic import BaseSettings
from pathlib import Path 
from dotenv import load_dotenv
# Defined .env path
env_path = Path(__file__).parent/'.env'

load_dotenv(dotenv_path=env_path)

# class Settings(BaseSettings):
#       mongodb_url: str = MONGODB_URL