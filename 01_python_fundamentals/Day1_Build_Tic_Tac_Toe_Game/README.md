## Goal:
Build a simple Tic-Tac-Toe game, playing against the computer. 

## Context and constraints:
As part of the 30 day coding challenge, the aim isn't perfection, but to ship a project each day, spending a maximum of 3 hours/day. Due to the time limit, some design choices and constraints were made when defining the scope.

## Design choices:
1. No OOP
2. Assign a mark to the player -> easier validation
3. Static board

## Project structure:

Day1_Build_Tic_Tac_Toe_Game/
├── README.md
├── notes_to_self.md
└── src/
    └── main.py

## Flow:
1. Game initialization
2. Welcome screen
3. Assign X or O to the player
4. Display instructions / board numbering
5. Create and display the empty board
6. Loop until game ends:
   - Player move (with input validation)
   - Update board
   - Check win/tie
   - Computer move (simple AI)
   - Update board
   - Check win/tie
7. Display winner or tie
8. Ask the player if they want to play again

## Tasks:
1. Display the board
2. Handle player input and mark it on the board
3. Validate player input (check for occupied or invalid positions)
4. Make the computer move
5. Keep the game running until an end condition is met
6. Check for win or tie:
   - Three consecutive marks (horizontal, vertical, diagonal)
   - No empty spaces left on the board
7. Announce the winner or tie
8. Offer a replay option

## Features Implemented:
- CLI-based gameplay
- Input validation
- Win condition checking
- Tie detection
- Basic AI strategy:
  - Win if possible
  - Block opponent
  - Take corner
  - Take center
  - Take edge
- Replay option