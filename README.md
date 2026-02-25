Google ADK - Tic Tac Toe Study Project

This is a study project developed with the Google ADK (Agent Development Kit). It allows a user to play Tic Tac Toe against an AI Agent that manages the game logic and communication.

Description
In this project, the AI Agent acts as a bridge between the player and the game logic (tictactoe.py).

Game Management: The agent handles game restarts, board visualization, and turn tracking.

Decision Making: The agent thinks of its own moves and processes the player's moves through the script.

Human-Friendly: It translates technical script returns into a conversational experience.

Requirements
Python: Developed using Python 3.12. Compatibility with older versions has not been tested.

Google ADK: You must have the Google ADK dependencies installed.

pip install google-adk

Setup & Execution
API Key Configuration:
You need a Google API Key to run the agent. Create a .env file in the project folder:

echo 'GOOGLE_API_KEY="YOUR_API_KEY"' > .env

Note: While the ADK supports other agents/backends, this project has only been tested with the Google Gemini API.

Run the Game:
To start playing, navigate to the project folder and run:

adk run .

Have fun!
