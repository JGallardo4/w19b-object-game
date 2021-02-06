class GameBoard:
    def __init__(self):
        self.winningRow = 11
        self.winningColumn = 3
        self.height = 11
        self.length = 13
        self.board = [
            self.createRow([]),
            self.createRow([6, 7, 8]),
            self.createRow([8]),
            self.createRow([1, 2, 3, 4, 6, 8, 9]),
            self.createRow([1, 4, 6, 8, 9]),
            self.createRow([1, 2, 4, 6, 8, 9, 10]),
            self.createRow([2, 4, 5, 6, 7, 8, 9, 10, 11]),
            self.createRow([2, 5, 7, 8, 11]),
            self.createRow([1, 2, 3, 5, 8, 9, 11]),
            self.createRow([1, 3, 5, 9, 11]),
            self.createRow([1, 3]),
            self.createRow([3]),
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    def checkWin(self, playerRow, playerColumn):
        return playerRow == self.winningRow and playerColumn == self.winningColumn

    def createRow(self, emptyCols):
        result = []

        for i in range (0, self.length):
            if(not i in emptyCols):
                result.append(" * ")
            else:
                result.append("   ")
        return result

