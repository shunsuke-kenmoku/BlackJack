class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        total = 0
        aces = 0

        for card in self.cards:
            value = card.value()
            total += value
            if card.rank == 'A':
                aces += 1

        # Aを11→1に変更する処理（バスト防止）
        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def show(self, hide_first=False):
        if hide_first:
            return ['??'] + [str(card) for card in self.cards[1:]]
        return [str(card) for card in self.cards]
