from enum import Enum


class Suits(Enum):
    SPADE = '♠'
    HEART = '♥'
    DIAMOND = '♦'
    CLUB = '♣'


class Ranks(Enum):
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'


class Card:
    def __init__(self, suit: Suits, rank: Ranks):
        self.suit = suit  # マーク（♠, ♥, ♦, ♣）
        self.rank = rank  # 数字や絵札（A, 2〜10, J, Q, K）

    def value(self) -> int:
        # 得点を返す
        if self.rank in {Ranks.JACK, Ranks.QUEEN, Ranks.KING}:
            return 10
        elif self.rank == Ranks.ACE:
            return 11  # Aの得点はあとで調整する、ここでは11。
        else:
            return int(self.rank.value)

    def __str__(self) -> str:
        return f"{self.rank.value}{self.suit.value}"
