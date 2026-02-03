from card.alias import Card
from card.enum import Color, Rank, Suit
from card.joker import Joker
from card.standard_card import StandardCard


def ndo(face_up: bool = True) -> list[Card]:
    deck: list[Card] = [
        Joker(Color.RED, face_up=face_up),
        Joker(Color.BLACK, face_up=face_up),
    ]
    for rank in Rank:
        deck.append(StandardCard(rank, Suit.SPADES, face_up=face_up))
    for rank in Rank:
        deck.append(StandardCard(rank, Suit.DIAMONDS, face_up=face_up))
    for rank in reversed(Rank):
        deck.append(StandardCard(rank, Suit.CLUBS, face_up=face_up))
    for rank in reversed(Rank):
        deck.append(StandardCard(rank, Suit.HEARTS, face_up=face_up))
    return deck
