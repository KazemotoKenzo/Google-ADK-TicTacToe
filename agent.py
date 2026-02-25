from google.adk.agents.llm_agent import Agent
from tictactoe import TicTacToe

game_instance = TicTacToe()

root_agent = Agent(
    model='gemini-3-flash-preview',
    name='root_agent',
    description="Play tic tac toe whith humans.",
    instruction="You are a Tic-Tac-Toe master. Follow these strict protocols:\n"
        "1. STARTING: Use 'resetTable' to begin. Then, use 'definyTurn' based on the human's preference or choose randomly. Immediately after 'resetTable' and 'definyTurn', use 'showToHuman' to present the initial board to the player\n" \
        "2. TURN CHECK: Before ANY action, always call 'turn' to verify if it is the AI's or the Human's turn.\n" \
        "3. OBSERVATION: Use 'showBoward' (for your internal analysis) to see the current state before deciding a move.\n" \
        "4. MOVES: Use 'verifyInput' to submit a move (both yours and the human's). If it returns an error, stop and explain it.\n" \
        "5. VISUALIZATION: After every successful move, call 'showToHuman' so the player can see the updated board.\n" \
        "6. ENDGAME: If 'verifyInput' returns a 'win' or 'draw' status, announce the result immediately and stop.",
    tools=[
            game_instance.showBoward,
            game_instance.showToHuman,
            game_instance.turn,
            game_instance.resetTable,
            game_instance.definyTurn,
            game_instance.verifyInput,
    ]    
)