"""
xxxDTO.model_dump()
"""

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class CreateUserDTO(BaseModel):
    username: str
    password: str
    email: EmailStr

class GetUserDTO(BaseModel):
    id: int
    username: str
    email: EmailStr

class PutUserDTO(BaseModel):
    username: str | None
    email: EmailStr | None
