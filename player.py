# Class representing a player
# Player has its name, its budget and list of cards

class Player:
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget
    self.cards = []

  def __repr__(self):
    return "The player {name} has the budget of {budget} dollars and has the following cards: {cards}".format(
      name = self.name, budget = self.budget, cards = ", ".join(self.cards) + "\n"
    )
  def change_name(self, name):
    self.name = name
    print("{name}'s name has changed to: ".format(name = self.name) + str(self.name) + "\n")
    
  def increase_budget(self, increase):
    self.budget += increase
    print("{name}'s budget has increased to: ".format(name = self.name) + str(self.budget) + "\n")
    
  def decrease_budget(self, decrease):
    self.budget -= decrease
    print("{name}'s budget has decreased to: ".format(name = self.name) + str(self.budget) + "\n")
  
  def add_card(self, card):
    self.cards.append(card)
    print("{name} has gained a new card: ".format(name = self.name) + str(card) + "\n")
  
  def remove_card(self, card):
    self.cards.remove(card)
    print("{card} has been removed of {name}'s inventory".format(card = card, name = self.name ) + str(card) + "\n")


  
player_1 = Player("Ivan", 1000)
print(player_1)
player_1.change_name("Ivan M")
print(player_1)
player_1.increase_budget(500)
print(player_1)
player_1.decrease_budget(200)
print(player_1)