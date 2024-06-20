// Code by melodingo 
// 13.06.2024

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Blackjack {
    private static final Random random = new Random();
    private static final String[] CARDS = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
    private static final String[] SUITS = {"♠", "♡", "♢", "♣"};

    public static void main(String[] args) {
        blackjack();
    }

    private static String generateRandomCard() {
        String card = CARDS[random.nextInt(CARDS.length)];
        String suit = SUITS[random.nextInt(SUITS.length)];
        return card + suit;
    }

    private static int calculateHandValue(List<String> hand) {
        int totalValue = 0;
        int numAces = 0;

        for (String card : hand) {
            String cardValue = card.substring(0, card.length() - 1);
            if ("JQK".contains(cardValue)) {
                totalValue += 10;
            } else if (cardValue.equals("A")) {
                totalValue += 11;
                numAces += 1;
            } else {
                totalValue += Integer.parseInt(cardValue);
            }
        }

        while (totalValue > 21 && numAces > 0) {
            totalValue -= 10;
            numAces -= 1;
        }

        return totalValue;
    }

    private static void printBlackjackTable(List<String> playerHand, List<String> dealerHand, boolean reveal) {
        int maxPlayerCardLength = playerHand.stream().mapToInt(String::length).max().orElse(0);
        int maxCardLength = Math.max(maxPlayerCardLength, 3);

        System.out.println("╔═══════════════════╗");
        System.out.println("║ Dealer's Cards:   ║");
        System.out.printf("║  [ %-"+maxCardLength+"s ]  [ %-"+maxCardLength+"s ] ║%n", dealerHand.get(0), reveal ? dealerHand.get(1) : "?");
        System.out.println("╠═══════════════════╣");
        System.out.println("║ Your Cards:       ║");
        System.out.printf("║  [ %-"+maxCardLength+"s ]   ║%n", String.join(" ]  [ ", playerHand));
        System.out.println("╠═══════════════════╣");
        System.out.println("║                   ║");
        System.out.println("║  [1] Hit          ║");
        System.out.println("║  [2] Stand        ║");
        System.out.println("╚═══════════════════╝");
    }

    private static void blackjack() {
        List<String> playerHand = new ArrayList<>();
        List<String> dealerHand = new ArrayList<>();
        playerHand.add(generateRandomCard());
        playerHand.add(generateRandomCard());
        dealerHand.add(generateRandomCard());
        dealerHand.add(generateRandomCard());

        printBlackjackTable(playerHand, dealerHand, false);

        Scanner scanner = new Scanner(System.in);

        while (true) {
            String input = scanner.nextLine();
            if (input.equals("1")) {
                playerHand.add(generateRandomCard());
                printBlackjackTable(playerHand, dealerHand, false);
                int playerValue = calculateHandValue(playerHand);
                if (playerValue > 21) {
                    System.out.println("╔══════════════════════════════════╗");
                    System.out.printf("║You busted! Your hand value is %d║%n", playerValue);
                    System.out.println("╚══════════════════════════════════╝");
                    break;
                } else if (playerValue == 21) {
                    System.out.println("╔═════════════════════════════════════════╗");
                    System.out.printf("║You got Blackjack! Your hand value is %d║%n", playerValue);
                    System.out.println("╚═════════════════════════════════════════╝");
                    break;
                } else {
                    continue;
                }
            } else if (input.equals("2")) {
                System.out.println("\nRevealing dealer's hidden card:");
                printBlackjackTable(playerHand, dealerHand, true);
                int dealerValue = calculateHandValue(dealerHand);
                int playerValue = calculateHandValue(playerHand);
                while (dealerValue < 17) {
                    dealerHand.add(generateRandomCard());
                    dealerValue = calculateHandValue(dealerHand);
                    System.out.println("\nDealer draws one card:");
                    printBlackjackTable(playerHand, dealerHand, true);
                }
                if (dealerValue > 21 || dealerValue < playerValue) {
                    System.out.println("╔═══════════════════════════════════╗");
                    System.out.printf("║You win! Dealer's hand value is %d ║%n", dealerValue);
                    System.out.println("╚═══════════════════════════════════╝");
                    break;
                } else if (dealerValue > playerValue) {
                    System.out.println("╔═══════════════════════════════════════╗");
                    System.out.printf("║Dealer wins! Dealer's hand value is %d ║%n", dealerValue);
                    System.out.println("╚═══════════════════════════════════════╝");
                    break;
                } else {
                    System.out.printf("It's a tie! Both you and the dealer have the same hand value: %d%n", playerValue);
                    break;
                }
            }
        }
        scanner.close();
    }
}

