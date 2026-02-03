from typing import Annotated, Literal

from card import Card, Joker, Rank, StandardCard, Suit
from card.alias import FaceCard, NumberCard

type Jewel = StandardCard[Literal[Rank.ACE], Suit]
type Trinket = NumberCard
type Trap = FaceCard
type Exit = Joker

type Temple = list[Card]
type Notes = Annotated[list[Card], "len<=3"]
type ScorePile = list[Card]
