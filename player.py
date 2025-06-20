from typing import List
from hand import Hand
from deck import Deck


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hand: Hand = Hand()

    def draw(self, deck: Deck) -> None:
        card = deck.draw()
        self.hand.add_card(card)
        print(f"{self.name} は {card} を引きました")

    def show_hand(self, hide_first: bool = False) -> List[str]:
        return self.hand.show(hide_first)

    def get_score(self) -> int:
        return self.hand.score()


class Dealer(Player):
    def __init__(self) -> None:
        super().__init__("ディーラー")

    def should_draw(self) -> bool:
        return self.get_score() < 17
