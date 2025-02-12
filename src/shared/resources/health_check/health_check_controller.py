from abc import ABC

from src.core.controller import Controller
from src.core.responses import MessageResponse


class HealthCheckController(Controller, ABC):
    def __init__(self):
        super().__init__(
            tags=['Utils']
        )

    async def handle(self) -> MessageResponse:
        return MessageResponse(message="ok")
