from typing import List
from card import Card, Ranks


class Hand:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def score(self) -> int:
        total = 0
        aces = 0

        for card in self.cards:
            value = card.value()
            total += value
            if card.rank == Ranks.ACE:
                aces += 1

        # Aを11→1に変更する処理（バスト防止）
        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def show(self, hide_first: bool = False) -> List[str]:
        if hide_first and len(self.cards) > 0:
            return ['??'] + [str(card) for card in self.cards[1:]]
        return [str(card) for card in self.cards]
