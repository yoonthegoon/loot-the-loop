from pathlib import Path
from typing import Self

import pygame as pg

from card import Card, Joker, ndo
from loot_the_loop.core import CoreGame


class Game:
    ASSETS_DIR: Path = Path(__file__).parent.parent / "assets"

    def __init__(self) -> None:
        self.screen_size: tuple[int, int] = (800, 600)
        self.game: CoreGame = CoreGame()
        self.card_surfaces: dict[str, pg.Surface] = {}

    def __enter__(self) -> Self:
        pg.init()
        self.screen: pg.Surface = pg.display.set_mode(self.screen_size)
        self.clock: pg.Clock = pg.time.Clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pg.quit()

    def draw_card(self, card: Card, dest: tuple[int, int]) -> None:
        card_surface = self.card_surfaces[str(card)]
        # TODO:
        #  - [ ] add border
        #  - [ ] add marker

        self.screen.blit(card_surface, dest)

    def load_card(self, card: Card) -> pg.Surface:
        file = self.ASSETS_DIR / "cards"
        if not card.face_up:
            file /= "10.svg"
        elif isinstance(card, Joker):
            file /= f"{card.color.value + 1}F.svg"
        else:
            file /= f"{card.suit.value}{card.rank.value:X}.svg"
        return pg.image.load(file).convert_alpha()

    def run(self) -> None:
        self.start()

        dt = 1 / 60
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.update(dt)

            pg.display.flip()
            dt = self.clock.tick(60) / 1000

    def start(self) -> None:
        deck = ndo()
        deck[1].flip()  # flip black joker for the card back
        for card in deck:
            self.card_surfaces[str(card)] = self.load_card(card)

    def update(self, dt: float) -> None:
        self.screen.fill(pg.Color(51, 115, 68))


if __name__ == "__main__":
    with Game() as game:
        game.run()
