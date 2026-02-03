from card import Card, Rank
from card.joker import Joker
from card.standard_card import StandardCard


def is_jewel(card: Card) -> bool:
    return isinstance(card, StandardCard) and card.rank == Rank.ACE


def is_trinket(card: Card) -> bool:
    return isinstance(card, StandardCard) and card.rank in [
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


def is_trap(card: Card) -> bool:
    return isinstance(card, StandardCard) and card.rank in [
        Rank.JACK,
        Rank.QUEEN,
        Rank.KING,
    ]


def is_exit(card: Card) -> bool:
    return isinstance(card, Joker)
