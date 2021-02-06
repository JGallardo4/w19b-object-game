from gameboard import GameBoard
import sprites

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

board = GameBoard()

while True:
    board.moveEnemies()
    if(board.checkEnemy()):
        print("You got bit by a venomous snake. You lose.")
        print("Score: 0")
        quit()
    
    board.printBoard()
    print("Coins: ", board.player.coins)
    selection = input("Make a move: ")    

    if(board.checkWin()):
        board.printBoard()
        print("You win!")
        print("Score: ", board.player.coins)
        quit()
    
    if(board.checkCoin()):
        board.player.getCoin()
        board.removeCoin()  
    
    board.movePlayer(selection)  
