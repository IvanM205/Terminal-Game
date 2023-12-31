from player import Player
from dealer import Dealer
from game import Game

def print_intro():
    intro = """
   _____ _            _    _            _    
  / ____| |          | |  | |          | |   
 | |    | | __ _  ___| | _| | __ _  ___| | __
 | |    | |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 | |____| | (_| | (__|   <| | (_| | (__|   < 
  \_____|_|\__,_|\___|_|\_\_|\__,_|\___|_|\_\\
    
    Welcome to Blackjack!
    Get as close to 21 as you can without going over!
    Try to beat the dealer!
    """
    print(intro)

print_intro()
name_player_1 = input("What is your name?: ")
player_1 = Player(name_player_1)
dealer = Dealer()
playing = True

# Game is in the loop so that the player can keep playing untill he runs out of the budget or he doesn't want to continue.
while playing == True:
    # Initialisation of a new game and of new card inventory for the player and the dealer.
    player_1.cards = []
    player_1.cards_values = []
    dealer.cards = []
    dealer.cards_values =[]
    game = Game(player_1, dealer)
    # Set up of a bet for the current game
    game.bet = int(input("Enter the bet: "))
    while game.bet > player_1.budget or game.bet < game.minimal_bet:
        if game.bet > player_1.budget:
            print("Too small budget. Input valid amount!")
        if game.bet < game.minimal_bet:
            print("Too small bet. Minimum bet is 25 dollars. Input valid amount!")
        game.bet = int(input("Enter the bet: "))
    player_1.budget -= game.bet
    # First two cards for the player.
    player_1.add_card(game.choose_card())
    player_1.add_card(game.choose_card())
    print(player_1)
    # Decision loop for the player to get new cards.
    new_cards = True
    while new_cards == True:
        match input("Do you want next card? (Yes/No): \n"):
            case "Yes":
                player_1.add_card(game.choose_card())
                player_1.set_cards_values()
                if not game.check_player_cards():
                    new_cards = False
                    print("{name} lost the game and lost the bet of {bet} dollars".format(name = player_1.name, bet = game.bet))
                    game.winner = "Dealer"
                    print(game)
            case "No":
                new_cards = False
        
            case _:
                print("Invalid input ! Write \"Yes\" or \"No\" ")
    # If the player didn't lost, dealer receives first two cards.
    if game.winner == "":
        dealer.add_card(game.choose_card())
        dealer.add_card(game.choose_card())
        dealer.set_cards_values()
        # Dealer continues to receive new cards until the cards value surpasses 17 or is equal to 17.
        while not game.has_dealer_enough():
            dealer.add_card(game.choose_card())
            dealer.set_cards_values()
            # If the dealer's cards value surpases 21 then the player won.
            if not game.check_dealer_cards():
                print("{name} has won the price of {bet} dollars.".format(name = player_1.name, bet = game.bet))
                player_1.budget += (2 * game.bet)
                game.winner = player_1.name
                print(game)
    # The player's and the dealer's cards are compared.
    if game.winner == "":
        player_1.set_cards_values()
        dealer.set_cards_values()
        if sum(player_1.cards_values) == sum(dealer.cards_values):
            print("It's a draw !")
            game.winner = "No one"
            player_1.budget += game.bet
            print(game)
        elif sum(player_1.cards_values) > sum(dealer.cards_values):
            print("{name} has won the price of {bet} dollars.".format(name = player_1.name, bet = game.bet))
            player_1.budget += (2 * game.bet)
            game.winner = player_1.name
            print(game)
        elif sum(player_1.cards_values) < sum(dealer.cards_values):
            print("{name} lost the game and lost the bet of {bet} dollars".format(name = player_1.name, bet = game.bet))
            game.winner = "Dealer"
            print(game)
    # If the player has big enough budget he gets a chance to keep playing if he decides to.
    if player_1.budget > game.minimal_bet:
        asking = True
        while asking:
            match input("Do you want to play again? (Yes/No): \n"):
                case "Yes":
                    asking = False
                case "No":
                    playing = False
                    asking = False
                    print("Game is over! Player {name} has finished with budget of {budget}".format(name = player_1.name, budget = player_1.budget))
                case _:
                    print(print("Invalid input ! Write \"Yes\" or \"No\" "))
                    asking = True
    else:
        playing = False
        print("Game is over! Player {name} has finished with budget of {budget}".format(name = player_1.name, budget = player_1.budget))
