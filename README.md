Strategic Grid Game
Overview
The Strategic Grid Game is a two-player grid-based game with AI capabilities, developed using Python and Pygame. It allows players to compete against each other or play against AI opponents, offering an engaging and strategic gameplay experience. The AI utilizes the Minimax algorithm to make optimal moves, adding a layer of challenge and intelligence to the game. The project also demonstrates the implementation of a Hash Table data structure with unit testing.

Features
Multiple Game Modes:
Human vs Human
Human vs AI
AI vs AI
AI Decision-Making:
The game uses the Minimax algorithm to simulate and evaluate potential moves, allowing AI players to make strategic decisions based on future board states.
Overflow Mechanics:
The game includes a recursive overflow mechanic, where gems spill over to adjacent cells when a certain threshold is reached, adding a level of complexity to the gameplay.
Interactive GUI:
The game’s Graphical User Interface (GUI), built with Pygame, features smooth animations, interactive elements, and color-coded pieces for each player to enhance the overall experience.
Save/Load Functionality:
Players can save and load game states using Python’s pickle module, allowing them to pause and resume games at any point.
Technologies Used
Programming Language: Python
Graphics Library: Pygame
AI Algorithm: Minimax Algorithm for AI decision-making
Data Structures: Queue for overflow management and Hash Table with separate chaining
Persistence: Python’s pickle module for saving/loading game states
Unit Testing: Python’s unittest module for testing Hash Table functionality
Game Mechanics
Hash Table Implementation: The project includes a custom-built hash table with separate chaining to handle collisions. This data structure is unit-tested using the Python unittest module to ensure correct functionality.
Overflow Mechanic: When a grid cell reaches a certain number of gems, they overflow into neighboring cells, potentially causing chain reactions that can change the state of the game rapidly.
AI with Minimax Algorithm: The AI uses a game tree and minimax algorithm to evaluate the best possible moves, considering both the player's and opponent's actions. The minimax algorithm is optimized for two-player games and ensures that the AI performs optimally.
Getting Started
Prerequisites:
Python 3.x
Pygame library
Installation:
Clone or download the repository from GitHub:
bash
Copy code
git clone <your-repo-url>
Install Pygame:
bash
Copy code
pip install pygame
Run the game:
bash
Copy code
python game.py
How to Play:
Start the game: Run the game.py file in your terminal.
Choose a game mode: Select from Human vs Human, Human vs AI, or AI vs AI.
Place gems: Click on a cell to place your gems. Pay attention to the overflow mechanic!
AI opponent: If you're playing against the AI, watch it make intelligent moves based on the minimax algorithm.
Save/Load:
Save Game: At any point during the game, you can save the current game state.
Load Game: Resume a saved game by loading the game state.
Future Enhancements
Alpha-Beta Pruning: Implementing alpha-beta pruning to improve AI performance by pruning unnecessary nodes in the game tree.
Improved Animations: Adding smoother transitions and more interactive elements to make the game visually appealing.
Unit Testing
The hash table implementation is tested using Python's unittest module. Unit tests ensure that all hash table functionalities (insertion, deletion, modification, and resizing) work correctly under various conditions.
