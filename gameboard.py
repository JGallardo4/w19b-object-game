import sprites
import random


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

        self.coins = [
            [1, 7],
            [3, 6],
            [3, 9],
            [5, 10],
            [8, 1],
            [8, 11],
            [9, 9],
            [10, 1]
        ]

        self.enemies = [
            sprites.Enemy(1, 6),
            sprites.Enemy(4, 9),
            sprites.Enemy(5, 9),
        ]

        self.player = sprites.Player(9, 11)

    def printBoard(self):
        enemyLocations = []
        
        for enemy in self.enemies:
            enemyLocations.append([enemy.rowPosition, enemy.columnPosition])
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == self.player.rowPosition and j == self.player.columnPosition:
                    print(" P ", end="")
                elif [i, j] in self.coins:
                    print(" 0 ", end="")
                elif [i, j] in enemyLocations:
                    print(" S ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    def checkWin(self):
        return self.player.rowPosition == self.winningRow and self.player.columnPosition == self.winningColumn

    def createRow(self, emptyCols):
        result = []

        for i in range(0, self.length):
            if(not i in emptyCols):
                result.append(" * ")
            else:
                result.append("   ")
        return result

    def checkCoin(self, row=-1, col=-1):
        if (row == -1 and col == -1):
            return [self.player.rowPosition, self.player.columnPosition] in self.coins
        else:
            return [row, col] in self.coins

    def checkEnemy(self):
        enemyLocations = []
        
        for enemy in self.enemies:
            enemyLocations.append([enemy.rowPosition, enemy.columnPosition])

        return [self.player.rowPosition, self.player.columnPosition] in enemyLocations

    def removeCoin(self):
        self.coins.remove([self.player.rowPosition, self.player.columnPosition])

    def movePlayer(self, selection):
        if(selection == "w"):
            if self.checkMove(self.player.rowPosition - 1, self.player.columnPosition):
                self.player.moveUp()
        elif(selection == "a"):
            if self.checkMove(self.player.rowPosition, self.player.columnPosition - 1):
                self.player.moveLeft()
        elif(selection == "s"):
            if self.checkMove(self.player.rowPosition + 1, self.player.columnPosition):
                self.player.moveDown()
        elif(selection == "d"):
            if self.checkMove(self.player.rowPosition, self.player.columnPosition + 1):
                self.player.moveRight()
        else:
            print("wrong input")

    def moveEnemies(self):
        for enemy in self.enemies:
            direction = random.randint(0, 3)

            if(direction == 0):
                if self.checkMove(enemy.rowPosition - 1, enemy.columnPosition) and not self.checkCoin(enemy.rowPosition - 1, enemy.columnPosition):
                    enemy.moveUp()
            elif(direction == 1):
                if self.checkMove(enemy.rowPosition, enemy.columnPosition - 1) and not self.checkCoin(enemy.rowPosition - 1, enemy.columnPosition):
                    enemy.moveLeft()
            elif(direction == 2):
                if self.checkMove(enemy.rowPosition + 1, enemy.columnPosition) and not self.checkCoin(enemy.rowPosition - 1, enemy.columnPosition):
                    enemy.moveDown()
            elif(direction == 3):
                if self.checkMove(enemy.rowPosition, enemy.columnPosition + 1) and not self.checkCoin(enemy.rowPosition - 1, enemy.columnPosition):
                    enemy.moveRight()
