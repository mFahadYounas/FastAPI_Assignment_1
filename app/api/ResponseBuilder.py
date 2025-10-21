from app.schemas.APIResponse import APIResponse
from typing import Optional


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
            return APIResponse(
                status=200,
                error="",
                data={
                    "id": id,
                    "item_name": item_name,
                    "existance": existance,
                    "temperature_celsius": temperature_celsius,
                },
            )
        return APIResponse(
            status=200,
            error="",
            data={
                "id": id,
                "item_name": item_name,
            },
        )

    @staticmethod
    def error(status: int, error: str):
        return APIResponse(status=status, error=error, data=None)
