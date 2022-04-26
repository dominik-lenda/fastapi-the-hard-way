from typing import Optional
from pydantic import BaseModel, EmailStr

class UserCrete(BaseModel):
    username: str
    email: EmailStr
    password: str