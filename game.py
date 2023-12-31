import random
# Lists representing the playing cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
deck = [[rank, suit] for suit in suits for rank in ranks]

class Game:
    counter = 0
    
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = 0
        self.winner = ""
        Game.counter += 1
        self.number = Game.counter
        self.minimal_bet = 25

    def __repr__(self):
        return "This is a game number {number} \n".format(number = self.number) + "Player {name} has bet {bet} dollars and received following cards: {cards_player} \n".format(name = self.player.name, bet = self.bet, cards_player = ", ".join([" of ".join([str(each) for each in card]) for card in self.player.cards])) + "Dealer received following cards: {cards_dealer} \n".format(cards_dealer = ", ".join([" of ".join([str(each) for each in card]) for card in self.dealer.cards])) + "The winner is: " + str(self.winner)
    
    def choose_card(self):
        return deck[random.randint(0, len(deck)-1)]

    def check_player_cards(self):
        if sum(self.player.cards_values) > 21 and 11 in self.player.cards_values:
            self.player.cards_values[self.player.cards_values.index(11)] = 1
            return True
        elif sum(self.player.cards_values) > 21:
            return False
        else:
            return True
        
    def check_dealer_cards(self):
        if sum(self.dealer.cards_values) > 21 and 11 in self.dealer.cards_values:
            self.dealer.cards_values[self.dealer.cards_values.index(11)] = 1
            return True
        elif sum(self.dealer.cards_values) > 21:
            return False
        else:
            return True

    def has_dealer_enough(self):
        if sum(self.dealer.cards_values) < 17:
            return False
        else:
            return True
    



        