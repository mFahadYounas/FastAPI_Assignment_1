from app.schemas.APIResponse import APIResponse
from typing import TypeVar, Generic

T = TypeVar("T")


class ResponseBuilder(Generic[T]):
    @staticmethod
    def success(
        data: T,
    ) -> APIResponse:
        return APIResponse[T](
            status=200,
            error="",
            data=data,
        )

    @staticmethod
    def error(status: int, error: str):
        return APIResponse[T](status=status, error=error, data=None)
