import pandas as pd
import numpy as np

class TicTacToe:
    def __init__(self):
        self.table = np.full((3, 3), " ")
        
    def reset_table(self):
        self.table.fill(" ")
    
    def printTable(self):
        text = ""
        for x in range(0,3):
            for i in range(0,3):
                text += ("| " if i == 1 else " ") + self.table[x, i] + (" |" if i == 1 else " ") 
            if x == 2: break
            text+= "\n-----------\n"
        print(text)

    def winCondition(self):
        if(self.table[0, 0] == self.table[0, 1] == self.table[0, 2] != " "):
            return True
        
        if(self.table[1, 0] == self.table[1, 1] == self.table[1, 2] != " "):
            return True
        
        if(self.table[2, 0] == self.table[2, 1] == self.table[2, 2] != " "):
            return True
        
        if(self.table[0, 0] == self.table[1, 1] == self.table[2, 2] != " "):
            return True
        
        if(self.table[0, 2] == self.table[1, 1] == self.table[2, 1] != " "):
            return True
        


    def maktest(self):
        self.table[0, 0] = "A"
        self.table[0, 1] = "B"
        self.table[0, 2] = "C"
        self.table[1, 0] = "D"
        self.table[1, 1] = "E"
        self.table[1, 2] = "F"
        self.table[2, 0] = "G"
        self.table[2, 1] = "H"
        self.table[2, 2] = "I"

game = TicTacToe()
game.maktest()
game.printTable()