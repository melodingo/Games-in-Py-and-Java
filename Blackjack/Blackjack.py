import random
import keyboard

def generate_random_card():
    all_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♡", "♢", "♣"]
    all_cards = [card + suit for card in all_cards for suit in suits]
    return random.choice(all_cards)

def print_blackjack_table(player_hand, dealer_hand, reveal=False):
    max_player_card_length = max(len(card) for card in player_hand)
    max_card_length = max(max_player_card_length, 3)
    print("╔═══════════════════╗")
    print("║ Dealer's Cards:   ║")
    print("║  [ {:<{}} ]  [ {:<{}} ] ║".format(dealer_hand[0], max_card_length, dealer_hand[1] if reveal else "?", max_card_length))
    print("╠═══════════════════╣")
    print("║ Your Cards:       ║")
    print("║  [ {:<{}} ]   ║".format("]  [ ".join(player_hand), max_card_length))
    print("╠═══════════════════╣")
    print("║                   ║")
    print("║  [1] Hit          ║")
    print("║  [2] Stand        ║")
    print("╚═══════════════════╝")

player_hand = [generate_random_card(), generate_random_card()]
dealer_hand = [generate_random_card(), generate_random_card()]
print_blackjack_table(player_hand, dealer_hand)

draw_count = 0

while True:
    if keyboard.is_pressed("enter"):
        print("\nRevealing dealer's hidden card:")
        print_blackjack_table(player_hand, dealer_hand, reveal=True)
    
    if keyboard.is_pressed_released("space") and draw_count < 2:
        player_hand.append(generate_random_card())
        draw_count += 1
        print_blackjack_table(player_hand, dealer_hand)

    if keyboard.is_pressed("esc"):
        break
