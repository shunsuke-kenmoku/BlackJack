from hand import Hand
from deck import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def draw(self, deck: Deck):
        card = deck.draw()
        self.hand.add_card(card)
        print(f"{self.name} は {card} を引きました")

    def show_hand(self, hide_first=False):
        return self.hand.show(hide_first)

    def get_score(self):
        return self.hand.score()


class Dealer(Player):
    def __init__(self):
        super().__init__("ディーラー")

    def should_draw(self):
        return self.get_score() < 17
