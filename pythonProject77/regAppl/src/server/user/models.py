from pydantic import BaseModel

class Basemodel_user(BaseModel):
    id: int
    name: str
    surname: str
    phone: str


class Basemodel_NewUser(BaseModel):
    name: str
    surname: str
    phone: str


class Update_user(BaseModel):
    name: str
    surname: str


class NewId(BaseModel):
    code: int
    id: int