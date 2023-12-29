# Class representing a player

class Player:
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget
    self.cards = []

  def __repr__(self):
    print("The player {name} has the budget of {budget} dollars and has the following cards: {cards}".format(
      name = self.name, budget = self.budget, cards = ", ".join(self.cards)
    ))
    
  def change_name(name):
    self.name = name
    print("The player's name has changed to: " + str(self.name) + "\n")
    
  def increase_budget(increase):
    self.budget += increase
    print("The player's budget has increased to: " + str(self.budget) + "\n")
    
  def decrease_budget(decrease):
    self.budget -= decrease
    print("The player's budget has decreased to: " + str(self.budget) + "\n")
  
  
    
