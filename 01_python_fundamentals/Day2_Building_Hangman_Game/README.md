## Goal:
Build a simple Hangman game.

## Context and constraints:
As part of the 30 day coding challenge, the aim isn't perfection, but to ship a project each day, spending a maximum of 3 hours/day. Due to the time limit, some design choices and constraints were made when defining the scope.

## Design choices:
1. List of words to choose from
2. Word to guess is represented by a row of dashes

## Project structure:

Day2_Building_Hangman_Game/
├── README.md
├── notes_to_self.md
└── src/
    └── main.py

## Flow:
1. Display word to be guessed represented by dashes
2. Display ABC
3. Ask for user input
4. Validate it
5. Mark the letter,  or reduce a life
6. Display
   - remaining letters of the ABC
   - letters guessed by the user
   - remaining lives
   - hanged man
7. Prompt user to keep playing
8. Loop until the man is hanged or the word is guessed
9. Result message
10. Ask to play again

## Tasks:
1. Define a list of words to guess
2. Represent the word as dashes
3. Display to user
4. Ask for user input
5. Ideally validate user input
   - don't reduce lives for the same guess
   - to limit the chance of same guess, display ABC and when a letter has been guessed remove it
   - display a list of already guessed letters
   - warn user about invalid characters, but don't reduce lives
6. Compare to the word and whether it contains the letter
7. If yes, place letter at correct position(s)
8. If not, decrease remaining lives and display hanging figure
9. End of game conditions: either the word is guessed, or the man is hanged
10. Display result, ask if the player wants to play again

## Features Implemented:
- Random word generation with `wonderwords`
- Input validation (single letter, no repeats)
- Track guessed letters and lives
- Text-based hangman figure
