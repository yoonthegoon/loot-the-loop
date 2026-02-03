from abc import ABC, abstractmethod
from typing import Self

from card.enum import Color


class BaseCard(ABC):
    def __init__(self, *, face_up: bool) -> None:
        self._face_up = face_up

    @property
    @abstractmethod
    def color(self) -> Color: ...

    @property
    def face_up(self) -> bool:
        return self._face_up

    def flip(self) -> Self:
        self._face_up = not self._face_up
        return self
