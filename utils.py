class PlayerMover:
    def __init__(self, player, board):
        self.player = player
        self.board = board

    def movePlayer(self, selection):        
        if(selection == "w"):
            if self.board.checkMove(self.player.rowPosition - 1, self.player.columnPosition):
                self.player.moveUp()
        elif(selection == "a"):
            if self.board.checkMove(self.player.rowPosition, self.player.columnPosition - 1):
                self.player.moveLeft()
        elif(selection == "s"):
            if self.board.checkMove(self.player.rowPosition + 1, self.player.columnPosition):
                self.player.moveDown()
        elif(selection == "d"):
            if self.board.checkMove(self.player.rowPosition, self.player.columnPosition + 1):
                self.player.moveRight()
        else:
            print("wrong input")