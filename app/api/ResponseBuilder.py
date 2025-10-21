from app.schemas.APIResponse import APIResponse
from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class ResponseBuilder(Generic[T]):
    @staticmethod
    def success(
        data: T,
        detail: Optional[bool],
    ) -> APIResponse:
        if detail:
            return APIResponse[T](
                status=200,
                error="",
                data=data,
            )
        return APIResponse[T](
            status=200,
            error="",
            data=data,
        )

    @staticmethod
    def error(status: int, error: str):
        return APIResponse[T](status=status, error=error, data=None)
