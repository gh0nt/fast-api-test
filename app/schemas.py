from pydantic import BaseModel
from datetime import datetime

# Esquema para creación de usuarios
class UserCreate(BaseModel):
    username: str
    useremail: str
    credit_card_number: str

# Esquema para respuestas de usuarios
class User(BaseModel):
    id: int
    username: str
    useremail: str
    credit_card_number: str
    created_timestamp: datetime

    class Config:
        orm_mode = True  
