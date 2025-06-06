"""

"""

from pydantic import BaseModel


class CreateClientDto(BaseModel):
    name: str    

class PutClientDto(BaseModel):
    name: str
    client_id: list[int]

class GetClientDto(BaseModel):
    name: str

class GetClientsQuery(BaseModel):
    page: int = 0
    page_size: int = 10