"""

"""

from pydantic import BaseModel

class CreateAccDto(BaseModel):
    name: str
    pwd: str
    host: str
    client_id: int

class PutAccDto(BaseModel):
    name: str
    pwd: str
    host: str