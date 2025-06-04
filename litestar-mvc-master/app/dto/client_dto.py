"""

"""

from pydantic import BaseModel

class CreateClientDto(BaseModel):
    name: str
    

class PutClientDto(BaseModel):
    name: str
    client_id: list[int]
