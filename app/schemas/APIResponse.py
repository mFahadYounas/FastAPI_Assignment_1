from pydantic import BaseModel
from typing import Optional, TypedDict, Required, NotRequired


class ResponseData(TypedDict):
    id: Required[int]
    item_name: Required[str]
    existance: NotRequired[str]
    temperature_celsius: NotRequired[float]


class APIResponse(BaseModel):
    status: int
    error: str
    data: Optional[ResponseData]
