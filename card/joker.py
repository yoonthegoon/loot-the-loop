from card.base import BaseCard
from card.enum import Color


class Joker[C: Color](BaseCard):
    def __init__(self, color: C, *, face_up: bool = True) -> None:
        super().__init__(face_up=face_up)
        self._color: C = color

    def __repr__(self) -> str:
        return f"Joker(color={self.color}, face_up={self.face_up})"

    def __str__(self) -> str:
        if not self.face_up:
            return chr(0x1F0A0)
        return chr(0x1F0AF + 0x10 * self.color.value)

    @property
    def color(self) -> C:
        return self._color
