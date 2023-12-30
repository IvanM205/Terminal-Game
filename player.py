# Class representing a player
# Player has its name, its budget and list of cards

class Player:
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget
    self.cards = []

  def __repr__(self):
    string_cards = []
    for card in self.cards:
      string_card = [str(each) for each in card]
      string_cards.append(string_card)
    if len(self.cards) == 0:
      return "The player {name} has the budget of {budget} dollars and has the following cards: {cards}".format(
        name = self.name, budget = self.budget, cards = "None" + "\n"
      )
    else:
      return "The player {name} has the budget of {budget} dollars and has the following cards: {cards}".format(
        name = self.name, budget = self.budget, cards = ", ".join([" of ".join(each) for each in string_cards]) + "\n"
      )
  def change_name(self, name):
    previous_name = self.name
    self.name = name
    print("{name}'s name has changed to: ".format(name = previous_name) + str(self.name) + "\n")
    
  def increase_budget(self, increase):
    self.budget += increase
    print("{name}'s budget has increased to: ".format(name = self.name) + str(self.budget) + "\n")
    
  def decrease_budget(self, decrease):
    self.budget -= decrease
    print("{name}'s budget has decreased to: ".format(name = self.name) + str(self.budget) + "\n")
  
  def add_card(self, card):
    self.cards.append(card)
    card = [str(i) for i in card]
    print("{name} has gained a new card: ".format(name = self.name) + " of ".join(card) + "\n")
  
  def remove_card(self, card):
    self.cards.remove(card)
    card = [str(i) for i in card]
    print("{card} has been removed of {name}'s inventory".format(card = " of ".join(card), name = self.name ) + "\n")

""" 
player_1 = Player("Ivan", 1000)
print(player_1)
player_1.change_name("Ivan M")
print(player_1)
player_1.increase_budget(500)
print(player_1)
player_1.decrease_budget(200)
print(player_1)
player_1.add_card([2, "Hearts"])
player_1.add_card([3, "Hearts"])
print(player_1)
player_1.remove_card([2, "Hearts"])
print(player_1)
"""