from random import Random
from typing import Literal

from card import ndo
from loot_the_loop.alias import Exit, Jewel, Notes, ScorePile, Temple, Trap, Trinket
from loot_the_loop.enum import Action, State
from loot_the_loop.exceptions import IllegalActionError


class Game:
    def __init__(self, random: Random = Random()) -> None:
        temple: Temple = ndo(face_up=False)
        random.shuffle(temple)
        self._temple: Temple = temple
        self._notes: Notes = []
        self._score_pile: ScorePile = []
        self._state: State = State.NON_TERMINAL

    @property
    def temple(self) -> Temple:
        return self._temple

    @property
    def notes(self) -> Notes:
        return self._notes

    @property
    def score_pile(self) -> ScorePile:
        return self._score_pile

    @property
    def state(self) -> State:
        return self._state

    @property
    def legal_actions(self) -> list[Action]:
        legal_actions: list[Action] = []
        top_card = self.temple[0]
        next_card = self.temple[1]
        if not top_card.face_up:
            legal_actions.append(Action.LOOK_AROUND)
        if (
            top_card.face_up
            and isinstance(top_card, Trinket)
            or next_card.face_up
            and isinstance(next_card, Trinket)
        ):
            legal_actions.append(Action.MARK_A_PATH)
        if top_card.face_up and isinstance(top_card, Trinket) and len(self.notes) < 3:
            legal_actions.append(Action.MARK_A_PATH)
        if len(self.notes) > 0:
            legal_actions.append(Action.RETURN_TO_A_MARKED_PATH)
        if len(legal_actions) == 0:
            self._state = State.LOST
        return legal_actions

    @property
    def score(self) -> int:
        if self.state == State.LOST:
            return 0
        return len(self.score_pile)

    def look_around(self) -> None:
        top_card = self.temple[0]
        next_card = self.temple[1]
        if not top_card.face_up:
            raise IllegalActionError(
                "look around can only be performed if the top card of the deck is face down"
            )
        top_card.flip()
        if not next_card.face_up:
            next_card.flip()

    def explore(self, index: Literal[0, 1]) -> None:
        card = self.temple[index]
        if not card.face_up or not isinstance(card, Trinket):
            raise IllegalActionError(
                "explore can only be performed if either or both of the top two cards in the deck are face-up number cards (trinkets)"
            )
        value = card.rank.value
        self._temple = self.temple[value:] + self.temple[:value]
        top_card = self.temple[0]
        if top_card.face_up:
            if isinstance(top_card, Jewel | Trinket):
                self._score_pile.append(self.temple.pop(0))
            elif isinstance(top_card, Trap):
                self._state = State.LOST
            elif (
                isinstance(top_card, Exit)
                and len(list(filter(lambda c: isinstance(c, Jewel), self.score_pile)))
                == 4
            ):
                self._state = State.WON

    def mark_a_path(self) -> None:
        top_card = self.temple[0]
        if (
            not top_card.face_up
            or not isinstance(top_card, Trinket)
            or len(self.notes) == 3
        ):
            raise IllegalActionError(
                "mark a path can only be performed if the top card of the deck is a face up number card (trinket), and you have less than three cards in your notes"
            )
        self.notes.append(self.temple.pop(0))

    def return_to_a_marked_path(self, index: Literal[0, 1, 2]) -> None:
        if len(self.notes) == 0:
            raise IllegalActionError(
                "return to a marked path can only be performed if you have at least one marked path in your notes"
            )
        self.temple.insert(0, self.notes.pop(index))
