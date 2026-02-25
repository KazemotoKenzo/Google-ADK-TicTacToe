from tictactoe import TicTacToe

game = TicTacToe()
game.resetTable(0)
print(game.definyTurn(1))
print(game.verifyInput("8"))
print(game.viewBoward())

print(game.verifyInput("8"))
print(game.verifyInput("6"))
print(game.viewBoward())

print(game.verifyInput("0"))
print(game.verifyInput("4"))
print(game.viewBoward())

print(game.verifyInput("2"))
print(game.verifyInput("1"))
print(game.viewBoward())

print(game.verifyInput("5"))
print(game.viewBoward())