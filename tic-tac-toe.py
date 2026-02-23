import pandas as pd
import numpy as np

class TicTacToe:
    arraymap = np.empty((3,3))

    def __init__(self):
        self.arraymap = np.full((3, 3), " ")
        
    def reset_table(self):
        self.arraymap.fill(" ")
    
    def printTable(self):
        print(" " + "X" + " | " + "X" + " | " + "X" + " ")
        print("===========")
        print(" " + "X" + " | " + "X" + " | " + "X" + " ")
        print("===========")
        print(" " + "X" + " | " + "X" + " | " + "X" + " ")

game = TicTacToe()
game.printTable()