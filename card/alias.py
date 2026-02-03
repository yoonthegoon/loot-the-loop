from typing import Literal

from card.enum import Black, Color, Rank, Red, Suit
from card.joker import Joker
from card.standard_card import StandardCard

type Card = StandardCard[Rank, Suit] | Joker[Color]

type NumberCard[S: Suit] = StandardCard[
    Literal[
        Rank.TWO,
        Rank.THREE,
        Rank.FOUR,
        Rank.FIVE,
        Rank.SIX,
        Rank.SEVEN,
        Rank.EIGHT,
        Rank.NINE,
        Rank.TEN,
    ],
    S,
]
type FaceCard[S: Suit] = StandardCard[Literal[Rank.JACK, Rank.QUEEN, Rank.KING], S]

type RedStandardCard[R: Rank] = StandardCard[R, Red]
type BlackStandardCard[R: Rank] = StandardCard[R, Black]
