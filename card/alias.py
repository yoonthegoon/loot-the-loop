from typing import Literal

from card.enum import Black, Rank, Red, Suit
from card.joker import Joker
from card.standard_card import StandardCard

type Card = StandardCard | Joker


class NumberCard[S: Suit](
    StandardCard[
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
): ...


class FaceCard[S: Suit](StandardCard[Literal[Rank.JACK, Rank.QUEEN, Rank.KING], S]): ...


class RedStandardCard[R: Rank](StandardCard[R, Red]): ...


class BlackStandardCard[R: Rank](StandardCard[R, Black]): ...
