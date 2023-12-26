from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Basemodel_car(BaseModel):
    id: int
    model: str
    data: Optional[datetime] = None
    defect: str


class restored_car(BaseModel):
    model: str
    defect: str

class Update_car(BaseModel):
    model: str
    defect: str

class NewId(BaseModel):
    code: int
    id: int
