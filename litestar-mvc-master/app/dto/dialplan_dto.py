"""

"""

from pydantic import BaseModel
from app.models.dialplan_model import DialplanStatus

class CreateDialplanDto(BaseModel):
    phone: str

class PutDialplanDto(BaseModel):
    phone: str
    status: DialplanStatus

class GetFreeDialplanDto(BaseModel):
    phone: str
