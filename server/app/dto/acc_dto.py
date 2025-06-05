"""

"""

from pydantic import BaseModel

class CreateAccDto(BaseModel):
    name: str
    pwd: str
    host: str
    # client_id: int

class PutAccDto(BaseModel):
    name: str
    pwd: str
    host: str

class GetAccDto(BaseModel):
    id: int
    name: str
    pwd: str
    host: str

class GetAccQuery(BaseModel):
    page: int = 1       # 页码
    page_size: int = 10 # 每页数量
