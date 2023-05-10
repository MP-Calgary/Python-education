import random

import os
# clear the terminal 
os.system('clear')

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    def is_owned(self):
        return self.owner is not None

class Board:
    def __init__(self, properties):
        self.properties = properties

    def get_property(self, index):
        return self.properties[index]

class Player:
    def __init__(self, name, money, board):
        self.name = name
        self.money = money
        self.position = 0
        self.properties = []
        self.board = board

    def move(self, steps):
        # Check if the player passed over the Go space
        if self.position + steps > 39:
            self.money += 200
            print("You passed over Go and earned $200!")
        self.position = (self.position + steps) % len(self.board.properties)

    def buy_property(self, property):
        if self.money >= property.price:
            self.money -= property.price
            property.owner = self
            self.properties.append(property)
            return True
        else:
            return False

    def sell_property(self, property):
        if property in self.properties:
            self.money += property.price
            property.owner = None
            self.properties.remove(property)
            return True
        else:
            return False

def play_game(players):
    board = Board([Property("Mediterranean Avenue", 60, 2),
                   Property("Baltic Avenue", 60, 4),
                   Property("Reading Railroad", 200, 25),
                   Property("Electric Company", 150, 0),
                   Property("Water Works", 150, 0)])
    num_players = len(players)
    current_player = 0
    game_over = False
    while not game_over:
        player = players[current_player]
        print("It's", player.name + "'s turn.")
        steps = random.randint(1, 6)
        print("Rolling the dice...", "You got", steps, "!")
        player.move(steps)
        print("You landed on", board.get_property(player.position).name + ".")
        if not board.get_property(player.position).is_owned():
            choice = input("Do you want to buy " + board.get_property(player.position).name + "? (y/n)")
            if choice == "y":
                if player.buy_property(board.get_property(player.position)):
                    print("Congratulations! You now own", board.get_property(player.position).name + ".")
                else:
                    print("Sorry, you don't have enough money to buy", board.get_property(player.position).name + ".")
        else:
            print(board.get_property(player.position).name + " is already owned by", board.get_property(player.position).owner.name + ".")
            rent = board.get_property(player.position).rent
            player.money -= rent
            board.get_property(player.position).owner.money += rent
            print("You paid", rent, "in rent to", board.get_property(player.position).owner.name + ".")
        print("Your current balance is", player.money, ".")
        if player.money <= 0:
            print("Sorry, you're bankrupt. Game over!")
            players.remove(player)
            num_players -= 1
        if num_players == 1:
            print(players[0].name + " wins!")
            game_over = True
        current_player = (current_player + 1) % num_players

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    players = []
    board = Board([Property("Mediterranean Avenue", 60, 2),
                   Property("Baltic Avenue", 60, 4),
                   Property("Reading Railroad", 200, 25),
                   Property("Electric Company", 150, 0),
                   Property("Water Works", 150, 0)])
    for i in range(num_players):
        name = input("Enter the name of player " + str(i+1) + ": ")
        money = int(input("Enter the starting balance for " + name + ": "))
        players.append(Player(name, money, board))

    play_game(players)
