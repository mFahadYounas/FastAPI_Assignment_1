from fastapi import HTTPException
from main import app
from app.schemas.Item import Item
from app.schemas.StoreItem import StoreItem
from app.api.ResponseBuilder import ResponseBuilder


@app.get("/item/{item_id}", response_model=Item)
async def get_items(item_id: int, detail: (bool | None) = None):
    try:
        int(item_id)
    except ValueError:
        return ResponseBuilder.error(
            status=400, error="Invalid item_id: item_id must be an integer!"
        )

    return ResponseBuilder.success(
        id=item_id,
        item_name="Milk",
        existance="In fridge",
        temperature_celsius=3.5,
        detail=detail,
    )


@app.post("/items/")
async def post_item(item: StoreItem):
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
