from pydantic import BaseModel


class StoreItem(BaseModel):
    name: str
    price: float
    quantity: int
