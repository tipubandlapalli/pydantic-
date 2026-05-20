from pydantic import BaseModel, computed_field, Field

class Booking(BaseModel):
    user_id: int
    price: int = 1000
    room_id: int
    nights: int = Field( ..., ge=1, le=15 )

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.nights

booking = Booking(
    user_id=1,
    room_id=1,
    nights=2
)
print(booking.total_price)
print(booking.model_dump())
print(booking) 