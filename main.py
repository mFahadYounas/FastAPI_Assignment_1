from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    item_name: str
    existance: Optional[None]
    temperature_celsius: Optional[float]


class StoreItem(BaseModel):
    name: str
    price: float
    quantity: int


@app.get("/item/{item_id}", response_model=Item)
def get_items(item_id: int, detail: Optional[bool]):
    try:
        int(item_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ID: ID must be integer")

    if detail:
        return {
            "id": item_id,
            "item_name": "Super Conducter",
            "existance": "future (may be)",
            "temperature_celsius": 0,
        }

    return {"id": item_id, "item_name": "Super Conductor"}


@app.post("/items/")
def post_item(item: StoreItem):
    if len(item.name) == 0:
        raise HTTPException(
            status_code=400, detail="Invalid name: Name can not be empty string"
        )
    if item.price < 0.0:
        raise HTTPException(
            status_code=400, detail="Invalid price: Price must be positive float number"
        )
    if item.quantity < 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid quantity: Quantity must be positive integer",
        )
    return item
