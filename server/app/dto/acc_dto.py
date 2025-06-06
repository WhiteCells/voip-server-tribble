"""

"""

from pydantic import BaseModel, Field, constr


class CreateAccDto(BaseModel):
    name: str
    pwd: str
    host: str    

class PutAccDto(BaseModel):
    name: str
    pwd: str
    host: str

class GetAccDto(BaseModel):
    id: str
    name: str
    pwd: str
    host: str
    # status: str
    # create_at: str

class GetAccQuery(BaseModel):
    page: int = 1       # 页码
    page_size: int = 10 # 每页数量
