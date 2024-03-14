import random
import keyboard

def generate_random_card():
    all_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits = ["♠", "♡", "♢", "♣"]
    all_cards = [card + suit for card in all_cards for suit in suits]
    return random.choice(all_cards)

def calculate_hand_value(hand):
    total_value = 0
    num_aces = 0
    for card in hand:
        if card[:-1] in ["J", "Q", "K"]:
            total_value += 10
        elif card[:-1] == "A":
            total_value += 11
            num_aces += 1
        else:
            total_value += int(card[:-1])
            
    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -= 1

    return total_value

def print_blackjack_table(player_hand, dealer_hand, reveal=False):
    max_player_card_length = max(len(card) for card in player_hand)
    max_card_length = max(max_player_card_length, 3)
    print("╔═══════════════════╗")
    print("║ Dealer's Cards:   ║")
    print("║  [ {:<{}} ]  [ {:<{}} ] ║".format(dealer_hand[0], max_card_length, dealer_hand[1] if reveal else "?", max_card_length))
    print("╠═══════════════════╣")
    print("║ Your Cards:       ║")
    print("║  [ {:<{}} ]    ║".format("]  [ ".join(player_hand), max_card_length))
    print("╠═══════════════════╣")
    print("║                   ║")
    print("║  [1] Hit          ║")
    print("║  [2] Stand        ║")
    print("╚═══════════════════╝")

def blackjack():
    player_hand = [generate_random_card(), generate_random_card()]
    dealer_hand = [generate_random_card(), generate_random_card()]

    print_blackjack_table(player_hand, dealer_hand)

    while True:
        if keyboard.is_pressed("1"):#gives new card when 1 is pressed
            player_hand.append(generate_random_card())
            print_blackjack_table(player_hand, dealer_hand)
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print("You busted! Your hand value is", player_value)
                break
            elif player_value == 21:
                print("You got Blackjack! Your hand value is", player_value)
                break
            else:
                continue
        
        if keyboard.is_pressed("2"):
            print("\nRevealing dealer's hidden card:")
            print_blackjack_table(player_hand, dealer_hand, reveal=True)
            dealer_value = calculate_hand_value(dealer_hand)
            while dealer_value < 17:
                dealer_hand.append(generate_random_card())
                dealer_value = calculate_hand_value(dealer_hand)
                print("\nDealer draws one card:")
                print_blackjack_table(player_hand, dealer_hand, reveal=True)
            if dealer_value > 21 or dealer_value < player_value:
                print("You win! Dealer's hand value is", dealer_value)
                break
            elif dealer_value > player_value:
                print("Dealer wins! Dealer's hand value is", dealer_value)
                break
            else:
                print("It's a tie! Both you and the dealer have the same hand value:", player_value)
                break

blackjack()
