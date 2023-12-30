from player import Player
from dealer import Dealer
from game import Game

player_1 = Player("Ivan", 1000)
dealer = Dealer()
game_1 = Game(player_1, dealer)

game_1.bet = int(input("Enter the bet: "))
player_1.add_card(game_1.choose_card())
player_1.add_card(game_1.choose_card())
player_1.budget -= game_1.bet
print(player_1)

new_cards = True
while new_cards == True:
    match input("Do you want next card? (Yes/No): \n"):
        case "Yes":
            player_1.add_card(game_1.choose_card())
            player_1.set_cards_values()
            print(player_1.cards_values)
            if not game_1.check_player_cards():
                new_cards = False
                print("User focked up")
                print("{name} lost the game and lost the bet of {bet} dollars".format(name = player_1.name, bet = game_1.bet))
                player_1.budget -= game_1.bet
                game_1.winner = "Dealer"
                print(game_1)
            

        case "No":
            new_cards = False
        
        case _:
            print("Invalid input ! Write \"Yes\" or \"No\" ")

if game_1.winner == "":
    dealer.add_card(game_1.choose_card())
    dealer.add_card(game_1.choose_card())
    dealer.set_cards_values()
    print(dealer.cards_values)

    while not game_1.has_dealer_enough():
        dealer.add_card(game_1.choose_card())
        dealer.set_cards_values()
        print(dealer.cards_values)
        if not game_1.check_dealer_cards():
            print("{name} has won the price of {bet} dollars.".format(name = player_1.name, bet = game_1.bet))
            player_1.budget += game_1.bet
            game_1.winner = player_1.name
            print(game_1)

if game_1.winner == "":
    player_1.set_cards_values()
    dealer.set_cards_values()

    if sum(player_1.cards_values) == sum(dealer.cards_values):
        print("It's a draw !")
        game_1.winner = "No one"
        print(game_1)
    elif sum(player_1.cards_values) > sum(dealer.cards_values):
        print("{name} has won the price of {bet} dollars.".format(name = player_1.name, bet = game_1.bet))
        player_1.budget += game_1.bet
        game_1.winner = player_1.name
        print(game_1)
    elif sum(player_1.cards_values) < sum(dealer.cards_values):
        print("{name} lost the game and lost the bet of {bet} dollars".format(name = player_1.name, bet = game_1.bet))
        player_1.budget -= game_1.bet
        game_1.winner = "Dealer"
        print(game_1)


    
        

"""
dealer = Dealer()
dealer.add_card([4, "Hearts"])
dealer.add_card([6, "Hearts"])
print(dealer)

game_1 = Game(player_1, dealer)
print(game_1)
game_2 = Game(player_1, dealer)
print(game_2)
"""