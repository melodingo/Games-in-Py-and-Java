import random
import keyboard

def generate_random_card():
    all_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♡", "♢", "♣"]
    all_cards = [card + suit for card in all_cards for suit in suits]
    return random.choice(all_cards)

def print_blackjack_table(player_hand, dealer_hand, reveal=False):
    print("╔═══════════════════╗")
    print("║ Dealer's Cards:   ║")
    print("║  [", dealer_hand[0], "]  [", end=" ")
    if reveal:
        print(dealer_hand[1], end=" ")
    else:
        print(" ? ", end=" ")
    print("]  ║")
    print("╠═══════════════════╣")
    print("║ Your Cards:       ║")
    print("║  [", end=" ")
    for card in player_hand:
        print(card, end=" ")
    print("]        ║")
    print("╠═══════════════════╣")
    print("║                   ║")
    print("║  [1] Hit          ║")
    print("║  [2] Stand        ║")
    print("╚═══════════════════╝")

player_hand = [generate_random_card(), generate_random_card()]
dealer_hand = [generate_random_card(), generate_random_card()]
print_blackjack_table(player_hand, dealer_hand)

if keyboard.is_pressed("enter"):
    print_blackjack_table(player_hand, dealer_hand, reveal=True)
