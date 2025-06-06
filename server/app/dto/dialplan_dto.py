"""

"""

from pydantic import BaseModel
from app.models.dialplan_model import DialplanStatus

class CreateDialplanDto(BaseModel):
    phone: str

class PutDialplanDto(BaseModel):
    phone: str
    status: DialplanStatus

class GetDialplanDto(BaseModel):
    id: str
    phone: str
    status: DialplanStatus

class GetFreeDialplanDto(BaseModel):
    id: str
    phone: str
