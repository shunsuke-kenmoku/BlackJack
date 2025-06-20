class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # マーク（♠, ♥, ♦, ♣）
        self.rank = rank  # 数字や絵札（A, 2〜10, J, Q, K）

    def value(self):
        # 得点を返す
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Aの得点はあとで調整する、ここでは11。
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"
