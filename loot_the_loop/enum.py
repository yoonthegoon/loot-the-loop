from enum import Enum, auto


class Action(Enum):
    LOOK_AROUND = auto()
    EXPLORE = auto()
    MARK_A_PATH = auto()
    RETURN_TO_A_MARKED_PATH = auto()


class State(Enum):
    NON_TERMINAL = auto()
    WON = auto()
    LOST = auto()
