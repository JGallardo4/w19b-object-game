from gameboard import GameBoard
from player import Player
from utils import PlayerMover

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

board = GameBoard()
player = Player(9, 11)
playerMover = PlayerMover(player, board)

while True:
    board.printBoard(player.rowPosition, player.columnPosition)
    print("Coins: ", player.coins)
    selection = input("Make a move: ")

    playerMover.movePlayer(selection)

    if(board.checkWin(player.rowPosition, player.columnPosition)):
        board.printBoard(player.rowPosition, player.columnPosition)
        print("You win!")
        quit()
    
    if(board.checkCoin(player.rowPosition, player.columnPosition)):
        player.getCoin()
        board.removeCoin(player.rowPosition, player.columnPosition)
    
    # Check if the player has won, if so print a message and break the loop!
