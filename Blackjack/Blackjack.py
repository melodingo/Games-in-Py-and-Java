import random

def print_blackjack_table(player_hand, dealer_hand, hidden_card=True):
    print("╔═══════════════════╗")
    print("║ Dealer's Cards:   ║")
    print("║  [ ? ]  [", end=" ")
    if hidden_card:
        print("? ]     ║")
    else:
        for card in dealer_hand[1:]:
            print(card, end=" ")
        print("]     ║")
    print("╠═══════════════════╣")
    print("║ Your Cards:       ║")
    print("║  [", end=" ")
    for card in player_hand:
        print(card, end=" ")
    print("]         ║")
    print("╠═══════════════════╣")
    print("║                   ║")
    print("║  [1] Another card ║")
    print("║  [2] Stand        ║")
    print("╚═══════════════════╝")

player_hand = ["10", "A"]
dealer_hand = ["7", "3"]
print_blackjack_table(player_hand, dealer_hand)
