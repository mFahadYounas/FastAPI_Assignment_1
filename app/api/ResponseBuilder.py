from app.schemas.APIResponse import APIResponse
from typing import Optional
from app.schemas.APIResponse import ItemResponseData


class ResponseBuilder:
    @staticmethod
    def success(
        id: int,
        item_name: str,
        existance: str,
        temperature_celsius: float,
        detail: Optional[bool],
    ) -> APIResponse:
        if detail:
            return APIResponse[ItemResponseData](
                status=200,
                error="",
                data={
                    "id": id,
                    "item_name": item_name,
                    "existance": existance,
                    "temperature_celsius": temperature_celsius,
                },
            )
        return APIResponse[ItemResponseData](
            status=200,
            error="",
            data={
                "id": id,
                "item_name": item_name,
            },
        )

    @staticmethod
    def error(status: int, error: str):
        return APIResponse[ItemResponseData](status=status, error=error, data=None)
