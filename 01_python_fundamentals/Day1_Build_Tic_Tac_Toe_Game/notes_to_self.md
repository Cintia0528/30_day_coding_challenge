## Refactor Notes:
- Migrate game logic from Jupyter notebook to src/main.py
- Remove global board dependency
- Structure code into clear sections:
  - Board utilities
  - Move logic
  - Game loop

## Possible Improvements:
1. In my current experiment, I assign X to the player, so when the player input is validated, I only need to validate the position, not both the mark and the position. Expand into checking the mark for
   - consistent use (player uses X in all rounds)
   - only allowed characters (only X, 0 and numbers 1-9)
   - assign X or 0 to players taking turns IF there is a rematch
2. Difficulty levels
3. OOP design
4. Keeping score of the games played
   - per session
   - forever