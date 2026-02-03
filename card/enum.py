from enum import Enum, auto
from typing import Literal


class Color(Enum):
    RED = auto()
    BLACK = auto()


class Rank(Enum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()


class Suit(Enum):
    SPADES = auto()
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()


Number = Literal[
    Rank.TWO,
    Rank.THREE,
    Rank.FOUR,
    Rank.FIVE,
    Rank.SIX,
    Rank.SEVEN,
    Rank.EIGHT,
    Rank.NINE,
    Rank.TEN,
]
Face = Literal[Rank.JACK, Rank.QUEEN, Rank.KING]

Red = Literal[Suit.HEARTS, Suit.DIAMONDS]
Black = Literal[Suit.SPADES, Suit.CLUBS]
