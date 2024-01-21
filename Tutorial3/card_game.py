import random


def get_shuffled_deck():
    """Initialize a list of 52 playing cards and return after shuffling, representing a shuffled deck of playing cards."""
    # suits and serial numbers
    suits = {'♣', '♠', '♦', '♥'}
    ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    deck = []
    # Create a 52-card deck of playing cards
    for suit in suits:
        for rank in ranks:
            deck.append(suit + ' ' + rank)
    random.shuffle(deck)
    return deck


def deal_card(deck, participant):
    """Deal a card to the participant"""
    card = deck.pop()
    participant.append(card)
    return card


def compute_total(hand):
    """Calculate and return the point sum of a hand"""
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, \
              '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    result = 0  # Initialize the sum of points to 0
    numAces = 0  # number of A

    # Calculate the number of points and Aces
    for card in hand:
        result += values[card[2:]]
        if card[2] == 'A':
            numAces += 1

    # If the sum of points is > 21, try to calculate A as 1
    # (so subtract 10), multiple A loops subtract 10 until the number of points <= 21
    while result > 21 and numAces > 0:
        result -= 10
        numAces -= 1
    return result


def print_hand(hand):
    for card in hand:
        print(card, end = '  ')
    print()


def blackjack():
    """Blackjack poker game, computer artificial intelligence AI is the dealer and the user is the player"""
    # Initialize a deck of shuffled playing cards, and initialize the cards in the dealer's and player's hands to be empty.
    deck = get_shuffled_deck()
    house = []  # dealer's card
    player = []  # player's cards

    # The player and the dealer are dealt two cards each in turn.
    for i in range(2):
        deal_card(deck, player)
        deal_card(deck, house)

    # Print a hand
    print('cards from the dealer：', end = '');
    print_hand(house)
    print('cards from the player：', end = '');
    print_hand(player)

    # Ask the player whether to continue taking cards, and if so, continue to deal cards to the player
    answer = input('Do you want to continue taking cards?（y/n，The default is y）：')
    while answer in ('', 'y', 'Y'):
        card = deal_card(deck, player)
        print('Cards the player gets are：', end = '');
        print_hand(player)
        # Calculate card points
        if compute_total(player) > 21:
            print('The player loses!')
            return
        answer = input('Do you want to continue taking cards?（y/n，The default is y）：')

    # The dealer determines whether to take the card according to the "dealer's rules"
    while compute_total(house) < 17:
        card = deal_card(deck, house)
        print('Cards the dealer gets：', end = '');
        print_hand(house)
        # Calculate card points
        if compute_total(house) > 21:
            print('The player loses!')
            return

    # Calculate the dealer's and player's points respectively, compare the point sizes, and output the winning or losing result information
    houseTotal, playerTotal = compute_total(house), compute_total(player)
    if houseTotal > playerTotal:
        print('The dealer wins!')
    elif houseTotal < playerTotal:
        print('player wins!')
    elif houseTotal == 21 and 2 == len(house) < len(player):  # The dealer with blackjack wins the card
        print('The dealer wins!')
    elif playerTotal == 21 and 2 == len(player) < len(house):  # The player with blackjack wins the card
        print('player wins!')
    else:
        print('draw！')


if __name__ == '__main__':
    blackjack()
