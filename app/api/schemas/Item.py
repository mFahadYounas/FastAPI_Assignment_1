from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    id: int
    item_name: str
    existance: Optional[str] = None
    temperature_celsius: Optional[float] = None
