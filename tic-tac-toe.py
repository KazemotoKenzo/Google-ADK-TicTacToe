import pandas as pd
import numpy as np

class TicTacToe:
    def __init__(self):
        #self.table = np.full((3, 3), " ")
        self.table = list(range(0,9))
        self.player1 = True
        self.count_plays = 0
        self.resetTable()
        
        
    def resetTable(self):
        for i in range(0,9):
            self.table[i] = str(i)

        #count = 0
        #for a in range(0,3):
        #    for b in range(0,3):
        #        self.table[a, b] = str(count)
        #        count += 1
    
    def printTable(self):
        text = ""
        for i in range(0,9):
            if (i == 3 or i == 6): text += "\n-----------\n"
            text += ("| " if (i == 1 or i == 4 or i == 7) else " ") + self.table[i] + (" |" if (i == 1 or i == 4 or i == 7) else " ") 


        #for a in range(0,3):
        #    for b in range(0,3):
        #        text += ("| " if b == 1 else " ") + self.table[a, b] + (" |" if b == 1 else " ") 
        #    if a == 2: break
        #    text+= "\n-----------\n"
        print(text)

    def winCondition(self):
        #if(self.table[0, 0] == self.table[0, 1] == self.table[0, 2] != " "):
        if self.table[0] == self.table[1] == self.table[2]:
            return True
        
        #if(self.table[1, 0] == self.table[1, 1] == self.table[1, 2] != " "):
        if self.table[3] == self.table[4] == self.table[5]:
            return True
        
        #if(self.table[2, 0] == self.table[2, 1] == self.table[2, 2] != " "):
        if self.table[6] == self.table[7] == self.table[8]:
            return True
        
        #if(self.table[0, 0] == self.table[1, 1] == self.table[2, 2] != " "):
        if self.table[0] == self.table[4] == self.table[8]:
            return True
        
        #if(self.table[0, 2] == self.table[1, 1] == self.table[2, 1] != " "):
        if self.table[2] == self.table[4] == self.table[6]:
            return True
        
        return False
    
    def drawCondition(self):
        if self.count_plays >= 9: return True
        return False
        
    def verifyInput(self, value):
        try:
            num = int(value)
            if 0 <= num <= 8:
                self.inputPlay(num)
                return True
            else:
                print("Número fora do intervalo permitido (0-8).")
                return False
        
        except ValueError:
            print("Erro: A entrada não é um número válido.")
            return False

    def inputPlay(self, value):
        if self.table[value] in ("X", "O"):
            print("Já está preenchido")
            return "Já está preenchido"
        self.table[value] = "X" if self.player1 else "O"
        if self.winCondition():
            print("Player X venceu!!" if self.player1 else "Player O venceu!!")
            return "Venceu"
        
        self.player1 = not self.player1
        self.count_plays += 1
        if self.drawCondition():
            print("Draw")
            return "Draw"
        
        


    #def maktest(self):
    #    self.table[0, 0] = "A"
    #    self.table[0, 1] = "B"
    #    self.table[0, 2] = "C"
    #    self.table[1, 0] = "D"
    #    self.table[1, 1] = "E"
    #    self.table[1, 2] = "F"
    #    self.table[2, 0] = "G"
    #    self.table[2, 1] = "H"
    #    self.table[2, 2] = "I"

game = TicTacToe()
game.printTable()

game.verifyInput("4")
game.verifyInput("0")
game.verifyInput("3")
game.verifyInput("1")
game.verifyInput("5")
game.verifyInput("2")
game.verifyInput("6")
game.verifyInput("7")
game.verifyInput("8")
game.printTable()