import time

class TicTacToe:
    def __init__(self):
        #self.table = np.full((3, 3), " ")
        self.table = list(range(0,9))
        self.playerX = True
        self.count_plays = 0
        self.player_turn = 0
        self.player_one = 0
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
        return text

        #for a in range(0,3):
        #    for b in range(0,3):
        #        text += ("| " if b == 1 else " ") + self.table[a, b] + (" |" if b == 1 else " ") 
        #    if a == 2: break
        #    text+= "\n-----------\n"
        

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
        
        if self.table[0] == self.table[3] == self.table[6]:
            return True
        
        #if(self.table[1, 0] == self.table[1, 1] == self.table[1, 2] != " "):
        if self.table[1] == self.table[4] == self.table[7]:
            return True
        
        #if(self.table[2, 0] == self.table[2, 1] == self.table[2, 2] != " "):
        if self.table[2] == self.table[5] == self.table[8]:
            return True

        #if(self.table[0, 0] == self.table[1, 1] == self.table[2, 2] != " "):
        if self.table[0] == self.table[4] == self.table[8]:
            return True
        
        #if(self.table[0, 2] == self.table[1, 1] == self.table[2, 1] != " "):
        if self.table[2] == self.table[4] == self.table[6]:
            return True
        
        return False
    
    def drawCondition(self):
        return self.count_plays >= 9
        
    def viewBoward(self):
        row1 = " ".join(self.table[0:3])
        row2 = " ".join(self.table[3:6])
        row3 = " ".join(self.table[6:9])
    
        return f"\n{row1}\n{row2}\n{row3}"
    
    def showBoward(self) -> dict:
        """View Boward"""

        return {
            "status": "succes",
            "current_boward": self.viewBoward()
        }
    
    def showToHuman(self) -> dict:
        """ShowBoward to Human"""
        return {
            "status": "success",
            "current_table_human_view" : self.printTable()
        }
    
    def turn(self) -> dict:
        """Verify if is human or AI turn"""
        return {
            "status": "success",
            "first_move": ("human" if self.player_one == self.player_turn else "AI") + " is the first to move"
        }

    def resetTable(self, first_move: int) -> dict:
        """
        Reset the game.
        Definy the first player: 0 to human, 1 to AI
        """
        for i in range(0,9):
            self.table[i] = str(i)
        
        self.count_plays = 0
        self.playerX = True

        return {
            "status": "success",
            "board_view": self.viewBoward()
        }


    def definyTurn(self, first_move: int) -> dict:
        """Definy the first player: 0 to human, 1 to AI"""
        if(first_move == 0):
            self.player_one = 0
        else: self.player_one = 1

        return {
                "status": "success",
                "first_move": ("human" if self.player_one == self.player_turn else "AI") + " is the first to move"
            }


    def verifyInput(self, input_: str) -> dict:
        """
        Execute a play in the boward.
        input_: is a string that need to bee a interger between '0' a '8' and represent a position that is not 'X' or 'O'.
        Return play's status and vizualize the boward.
        """
        time.sleep(20)

        try:
            num = int(input_)
            if 0 <= num <= 8:
                return self.inputPlay(num)
            else:
                #print("Número fora do intervalo permitido (0-8).")
                return {
                    "status": "error", 
                    "input": "input " + input_ + " need to be a integer between 0 and 8"
                }
        
        except ValueError:
            #print("Erro: A entrada não é um número válido.")
            return {
                    "status": "error", 
                    "input": "The" + input_ + "is not valid"
            }
        
    def inputPlay(self, value):
        if self.table[value] in ("X", "O"):
            # "Já está preenchido"
            return {
                "status": "error", 
                "input": "Position is already placed, try choose another position"
            }
        
        self.table[value] = "X" if self.playerX else "O"
        
        if self.winCondition():
            #print("Player X venceu!!" if self.player1 else "Player O venceu!!")
            return {
                "status": "success", 
                "win": ("Human" if self.player_one == self.player_turn else "AI") + " win"
            }
        
        if self.drawCondition():
            #print("Draw")
            return {
                "status": "success", 
                "win": "Draw"
            }
        
        self.playerX = not self.playerX
        self.count_plays += 1
        self.player_turn += 1
        if(self.player_turn > 1) : self.player_turn = 0

        return {
            "status": "success", 
            "input": "Success placed",
            "board_view": self.viewBoward()
        }