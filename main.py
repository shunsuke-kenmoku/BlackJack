from deck import Deck
from player import Player, Dealer
import time


def main():
    deck = Deck()
    player = Player("あなた")
    dealer = Dealer()

    # 最初に2枚ずつ配る
    for _ in range(2):
        player.draw(deck)
        dealer.draw(deck)

    # プレイヤーのターン
    while True:
        print("\nあなたの手札:", player.show_hand())
        print("あなたの得点:", player.get_score())
        print("ディーラーの見えているカード:", dealer.show_hand(hide_first=True))

        if player.get_score() > 21:
            print("バースト！あなたの負けです。")
            return

        choice = input("カードを引きますか？ (H = ヒット、その他 = スタンド): ").upper()
        if choice == 'H':
            player.draw(deck)
        else:
            break

    # ディーラーのターン
    print("\nディーラーのターン")
    print("ディーラーの手札:", dealer.show_hand(hide_first=False))
    while dealer.should_draw():
        time.sleep(1)
        dealer.draw(deck)
        print("ディーラーの得点:", dealer.get_score())

    # 結果発表
    player_score = player.get_score()
    dealer_score = dealer.get_score()

    print("\n=== 最終結果 ===")
    print("あなたの得点:", player_score)
    print("ディーラーの得点:", dealer_score)

    if dealer_score > 21:
        print("ディーラーがバースト！あなたの勝ち！")
    elif player_score > dealer_score:
        print("あなたの勝ち！")
    elif player_score < dealer_score:
        print("ディーラーの勝ち！")
    else:
        print("引き分けです！")


if __name__ == "__main__":
    main()
