# this is for List, Dict, Optional

from pydantic import BaseModel
from typing import List, Dict, Optional
from pydantic import Field

class Cart(BaseModel):
    user_id: int
    items: List[str]
    rating: float = Field(
        ...,
        ge=0.0,
        le=10,
        description="Your rating for your cart selection",
        examples=6.67
    )
    quant: Dict[str, int]
    image: Optional[str] = None

input_data = {
    'user_id': 1,
    'items':["ball"],
    'quant': {"ball":1},
}


cart = Cart(**input_data)
print(cart)
