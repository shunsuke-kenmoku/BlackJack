import random
from card import Card  # card.py の Card クラスを使う


class Deck:

    def __init__(self):
        suits = ['♠', '♦', '♥', '♣']  # スート（マーク）
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'J', 'Q', 'K']  # 長いので折り返し
        self.cards = [
            Card(suit, rank)
            for suit in suits
            for rank in ranks
        ]
        random.shuffle(self.cards)  # シャッフル

    def draw(self):
        if len(self.cards) == 0:
            raise Exception("デッキが空です！")
        return self.cards.pop()  # 1枚引く
