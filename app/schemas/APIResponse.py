from pydantic import BaseModel
from typing import Optional, TypedDict, Required, NotRequired, TypeVar, Generic


T = TypeVar("T")


class ItemResponseData(TypedDict):
    id: Required[int]
    item_name: Required[str]
    existance: NotRequired[str]
    temperature_celsius: NotRequired[float]


class APIResponse(BaseModel, Generic[T]):
    status: int
    error: str
    data: Optional[T]
