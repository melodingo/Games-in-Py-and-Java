// Code by melodingo 
// 13.06.2024

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Blackjack {
    private static final Random random = new Random(); // Random object to generate random values
    private static final String[] CARDS = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}; // Card values
    private static final String[] SUITS = {"♠", "♡", "♢", "♣"}; // Card suits
    private static double playerBalance = 100.0;  // Starting balance for the player

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Scanner object for reading user input
        while (true) { // Main menu loop
            showMenu(); // Display the menu
            String menuChoice = scanner.nextLine(); // Read the user's menu choice
            if (menuChoice.equalsIgnoreCase("P")) { // Start the game if 'P' is pressed
                startGame(scanner); // Start the game loop
            } else if (menuChoice.equalsIgnoreCase("E")) { // Exit the game if 'E' is pressed
                break;
            } else {
                System.out.println("Invalid choice. Please enter 'P' to play or 'E' to exit."); // Invalid input handling
            }
        }
        scanner.close(); // Close the scanner
    }

    private static void showMenu() {
        // Display the main menu
        System.out.println("╔═════════════════════════╗");
        System.out.println("║ Welcome to Blackjack!   ║");
        System.out.println("║                         ║");
        System.out.println("║ [P] Play                ║");
        System.out.println("║ [E] Exit                ║");
        System.out.println("╚═════════════════════════╝");
        System.out.print("Please make a selection: ");
    }

    private static void startGame(Scanner scanner) {
        while (true) { // Game loop
            System.out.printf("Your current balance: $%.2f%n", playerBalance); // Display current balance
            System.out.println("Enter your bet amount (or type 'menu' to return to the main menu):");
            String betInput = scanner.nextLine(); // Read bet amount or menu command
            if (betInput.equalsIgnoreCase("menu")) { // Return to menu
                break;
            }
            double betAmount;
            try {
                betAmount = Double.parseDouble(betInput); // Parse the bet amount
                if (betAmount > playerBalance) { // Check if bet exceeds balance
                    System.out.println("You cannot bet more than your current balance.");
                    continue;
                }
                if (betAmount <= 0) { // Check for invalid bet amount
                    System.out.println("Please enter a valid bet amount.");
                    continue;
                }
            } catch (NumberFormatException e) { // Handle non-numeric input
                System.out.println("Invalid input. Please enter a numerical value.");
                continue;
            }

            int gameResult = blackjack(betAmount); // Play a round of Blackjack (1: win, -1: lose, 0: draw)
            if (gameResult == 1) {
                playerBalance += betAmount; // Update balance for win
            } else if (gameResult == -1) {
                playerBalance -= betAmount; // Update balance for loss
            }

            if (playerBalance <= 0) { // Check for game over condition
                System.out.println("You are out of money! Game over.");
                playerBalance = 100.0;
                break;
            }
        }
    }

    private static String generateRandomCard() {
        String card = CARDS[random.nextInt(CARDS.length)]; // Randomly select a card value
        String suit = SUITS[random.nextInt(SUITS.length)]; // Randomly select a card suit
        return card + suit; // Return the combined card
    }

    private static int calculateHandValue(List<String> hand) {
        int totalValue = 0; // Total value of the hand
        int numAces = 0; // Number of Aces in the hand

        for (String card : hand) {
            String cardValue = card.substring(0, card.length() - 1); // Extract the card value
            if ("JQK".contains(cardValue)) { // Face cards (J, Q, K) are worth 10 points
                totalValue += 10;
            } else if (cardValue.equals("A")) { // Ace can be worth 11 points
                totalValue += 11;
                numAces += 1;
            } else { // Numeric cards are worth their value
                totalValue += Integer.parseInt(cardValue);
            }
        }

        while (totalValue > 21 && numAces > 0) { // Adjust for Aces if total value exceeds 21
            totalValue -= 10;
            numAces -= 1;
        }

        return totalValue; // Return the total hand value
    }

    private static void printBlackjackTable(List<String> playerHand, List<String> dealerHand, boolean reveal) {
        int maxPlayerCardLength = playerHand.stream().mapToInt(String::length).max().orElse(0); // Get max card length for player
        int maxCardLength = Math.max(maxPlayerCardLength, 3); // Determine max card length for formatting

        System.out.println("╔═══════════════════╗");
        System.out.println("║ Dealer's Cards:   ║");
        System.out.printf("║  [ %-"+maxCardLength+"s ]  [ %-"+maxCardLength+"s ] ║%n", dealerHand.get(0), reveal ? dealerHand.get(1) : "?"); // Show dealer's cards, reveal second if true
        System.out.println("╠═══════════════════╣");
        System.out.println("║ Your Cards:       ║");
        System.out.printf("║  [ %-"+maxCardLength+"s ]   ║%n", String.join(" ]  [ ", playerHand)); // Show player's cards
        System.out.println("╠═══════════════════╣");
        System.out.println("║                   ║");
        System.out.println("║  [1] Hit          ║");
        System.out.println("║  [2] Stand        ║");
        System.out.println("╚═══════════════════╝");
    }

    private static int blackjack(double betAmount) {
        List<String> playerHand = new ArrayList<>(); // Initialize player's hand
        List<String> dealerHand = new ArrayList<>(); // Initialize dealer's hand
        playerHand.add(generateRandomCard()); // Deal two cards to player
        playerHand.add(generateRandomCard());
        dealerHand.add(generateRandomCard()); // Deal two cards to dealer
        dealerHand.add(generateRandomCard());

        printBlackjackTable(playerHand, dealerHand, false); // Print initial game table

        Scanner scanner = new Scanner(System.in); // Scanner for reading player input

        while (true) { // Player action loop
            String input = scanner.nextLine(); // Read player action
            if (input.equals("1")) { // Player chooses to hit
                playerHand.add(generateRandomCard()); // Add a card to player's hand
                printBlackjackTable(playerHand, dealerHand, false); // Print updated game table
                int playerValue = calculateHandValue(playerHand); // Calculate player's hand value
                if (playerValue > 21) { // Check for bust
                    System.out.println("╔══════════════════════════════════╗");
                    System.out.printf("║You busted! Your hand value is %d ║%n", playerValue);
                    System.out.println("╚══════════════════════════════════╝");
                    return -1; // Player loses
                } else if (playerValue == 21) { // Check for Blackjack
                    System.out.println("╔═════════════════════════════════════════╗");
                    System.out.printf("║You got Blackjack! Your hand value is %d║%n", playerValue);
                    System.out.println("╚═════════════════════════════════════════╝");
                    return 1; // Player wins
                } else {
                    continue; // Continue the loop if hand value is less than 21
                }
            } else if (input.equals("2")) { // Player chooses to stand
                System.out.println("\nRevealing dealer's hidden card:");
                printBlackjackTable(playerHand, dealerHand, true); // Reveal dealer's hidden card
                int dealerValue = calculateHandValue(dealerHand); // Calculate dealer's hand value
                int playerValue = calculateHandValue(playerHand); // Calculate player's hand value
                while (dealerValue < 17) { // Dealer draws cards until hand value is 17 or more
                    dealerHand.add(generateRandomCard());
                    dealerValue = calculateHandValue(dealerHand);
                    System.out.println("\nDealer draws one card:");
                    printBlackjackTable(playerHand, dealerHand, true); // Print updated game table
                }
                if (dealerValue > 21 || dealerValue < playerValue) { // Dealer busts or player has higher value
                    System.out.println("╔═══════════════════════════════════╗");
                    System.out.printf("║You win! Dealer's hand value is %d ║%n", dealerValue);
                    System.out.println("╚═══════════════════════════════════╝");
                    return 1; // Player wins
                } else if (dealerValue > playerValue) { // Dealer has higher value
                    System.out.println("╔═══════════════════════════════════════╗");
                    System.out.printf("║Dealer wins! Dealer's hand value is %d ║%n", dealerValue);
                    System.out.println("╚═══════════════════════════════════════╝");
                    return -1; // Dealer wins
                } else {
                    System.out.printf("It's a tie! Both you and the dealer have the same hand value: %d%n", playerValue);
                    return 0; // Tie
                }
            }
        }
    }
}
