from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {"id": 101, 'name':"tipu", 'is_active': "tipu"}

user = User(**input_data)

# makes it type safe 
print(user) 