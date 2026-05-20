from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product_one = Product(id=1, name='tipu', in_stock=False)

# field requrired errors help : by pydantic
print(product_one)