# Class representing a dealer
class Dealer:

    def __init__(self):
        self.cards = []
        self.cards_values = []

    def __repr__(self):
        string_cards = []
        for card in self.cards:
            string_card = [str(each) for each in card]
            string_cards.append(string_card)
        return "The dealer has the following cards: {cards}".format(cards = ", ".join([" of ".join(each) for each in string_cards])) + "\n"

    def add_card(self, card):
        self.cards.append(card)
        card = [str(i) for i in card]
        print("The dealer has gained a new card: " + " of ".join(card) + "\n")
    
    def remove_card(self, card):
        self.cards.remove(card)
        card = [str(i) for i in card]
        print("{card} has been removed of the dealer's inventory".format(card = " of ".join(card)) + "\n")
    
    def set_cards_values(self):
        self.cards_values = []
        for card in self.cards:
            if type(card[0]) is str:
                if card[0] == "Ace":
                  self.cards_values.append(11)
                else:
                    self.cards_values.append(10)
            else:
                self.cards_values.append(card[0])
        while 11 in self.cards_values and sum(self.cards_values) > 21:
            self.cards_values[self.cards_values.index(11)] = 1

"""
dealer = Dealer()
print(dealer)
dealer.add_card([4, "Hearts"])
dealer.add_card([6, "Hearts"])
print(dealer)
dealer.remove_card([4, "Hearts"])
print(dealer)
"""