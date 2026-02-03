from typing import Annotated, Literal

from card import Card, Joker, Rank, StandardCard, Suit
from card.alias import FaceCard, NumberCard


class Jewel(StandardCard[Literal[Rank.ACE], Suit]): ...


class Trinket(NumberCard): ...


class Trap(FaceCard): ...


class Exit(Joker): ...


type Temple = list[Card]
type Notes = Annotated[list[Card], "len<=3"]
type ScorePile = list[Card]
