from typing import Literal, overload

from card.base import BaseCard
from card.enum import Black, Color, Rank, Red, Suit


class StandardCard[R: Rank, S: Suit](BaseCard):
    def __init__(self, rank: R, suit: S, *, face_up: bool = True) -> None:
        super().__init__(face_up=face_up)
        self._rank = rank
        self._suit = suit

    def __repr__(self) -> str:
        return (
            f"StandardCard(rank={self.rank}, suit={self.suit}, face_up={self.face_up})"
        )

    def __str__(self) -> str:
        if not self.face_up:
            return chr(0x1F0A0)
        return chr(0x1F090 + 0x10 * self.suit.value + self.rank.value)

    @property
    def rank(self) -> R:
        return self._rank

    @property
    def suit(self) -> S:
        return self._suit

    @overload
    def color(
        self: "StandardCard[Rank, Literal[Suit.SPADES]]",
    ) -> Literal[Color.BLACK]: ...

    @overload
    def color(
        self: "StandardCard[Rank, Literal[Suit.HEARTS]]",
    ) -> Literal[Color.BLACK]: ...

    @overload
    def color(
        self: "StandardCard[Rank, Literal[Suit.DIAMONDS]]",
    ) -> Literal[Color.BLACK]: ...

    @overload
    def color(
        self: "StandardCard[Rank, Literal[Suit.CLUBS]]",
    ) -> Literal[Color.BLACK]: ...

    @overload
    def color(self: "StandardCard[Rank, Red]") -> Literal[Color.RED]: ...

    @overload
    def color(self: "StandardCard[Rank, Black]") -> Literal[Color.BLACK]: ...

    @property
    def color(self) -> Color:
        match self.suit:
            case Suit.HEARTS | Suit.DIAMONDS:
                return Color.RED
            case Suit.SPADES | Suit.CLUBS:
                return Color.BLACK
