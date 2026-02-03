from typing import Annotated, Literal

from card import Card, Color, Joker, Rank, StandardCard, Suit
from card.alias import FaceCard, NumberCard

type Jewel = StandardCard[Literal[Rank.ACE], Suit]
type Trinket = NumberCard[Suit]
type Trap = FaceCard[Suit]
type Exit = Joker[Color]

type Temple = list[Card]
type Notes = Annotated[list[Card], "len<=3"]
type ScorePile = list[Card]
