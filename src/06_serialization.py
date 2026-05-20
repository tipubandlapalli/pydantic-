from pydantic import BaseModel, ConfigDict
from typing import List

class Address(BaseModel):
    street: str
    house_no: str

class User(BaseModel):
    name: str
    address: Address
    email: str
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m=Y %')}
    )
