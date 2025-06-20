import random
from typing import List
from card import Card, Suits, Ranks  # card.py の Card,Suits クラスを使う


class Deck:

    def __init__(self):
        self.cards: List[Card] = [
            Card(suit, rank)
            for suit in Suits
            for rank in Ranks
        ]
        random.shuffle(self.cards)  # シャッフル

    def draw(self) -> Card:
        if len(self.cards) == 0:
            raise Exception("デッキが空です！")
        return self.cards.pop()  # 1枚引く
