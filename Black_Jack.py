import random

kinds = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
levels = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")
values = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
          "jack": 10, "queen": 10, "king": 10, "ace": 11}
playing = True


class Card:
    def __init__(self, kind, level):
        self.kind = kind
        self.level = level

    def __str__(self):
        return self.level + ' of ' + self.kind


class Deck:

    def __init__(self):
        self.deck = []  # storage
        for kind in kinds:
            for level in levels:
                self.deck.append(Card(kind, level))

    def __str__(self):
        deck_cards = ''
        for card in self.deck:
            deck_cards += '\n' + card.__str__()
        return deck_cards

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.level]
        if card.level == 'ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Insert your bet: '))
        except ValueError:
            print("that's not integer")
            continue
        else:
            if chips.bet > chips.total:
                print('Your bet more than your total chips', chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? h or s?')
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player chose stand, dealer is playing')
            playing = False
        else:
            print('please try again')
            continue
        break


def show_some(player, dealer):
    print("\n Dealer's Hand")
    print("Hidden Card")
    print(" ", dealer.cards[1])
    print("\n Player's Hand", *player.cards, sep='\n')


def show_all(player, dealer):
    print("\n Dealer's Card", *dealer.cards, sep='\n')
    print('Dealer Card', dealer.value)
    print("\n Player's Card", *player.cards, sep='\n')
    print("Player's Card", player.value)


def player_bust(player, dealer, chips):
    print('Player Bust')
    chips.lose_bet()


def player_win(player, dealer, chips):
    print('Player win')
    chips.win_bet()


def dealer_bust(player, dealer, chips):
    print('Dealer Bust')
    chips.win_bet()


def dealer_win(player, dealer, chips):
    print('Dealer Win')
    chips.lose_bet()


def push(player, dealer):
    print("player's and dealer's value are same")


while True:
    print(
        'Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand, dealer_hand, player_chips)

        elif player_hand.value > dealer_hand.value:
            player_win(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)
    # Inform Player of their chips total
    print("\nPlayer Won", player_chips.total)
    # Ask to play again
    new_game = input("do you wanna play again? y or n?")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("thanks for playing")
        break