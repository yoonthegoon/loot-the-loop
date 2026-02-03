from card.enum import Black, Face, Number, Rank, Red, Suit
from card.joker import Joker
from card.standard_card import StandardCard

Card = StandardCard | Joker

type NumberCard[S: Suit] = StandardCard[Number, S]
type FaceCard[S: Suit] = StandardCard[Face, S]

type RedStandardCard[R: Rank] = StandardCard[R, Red]
type BlackStandardCard[R: Rank] = StandardCard[R, Black]
