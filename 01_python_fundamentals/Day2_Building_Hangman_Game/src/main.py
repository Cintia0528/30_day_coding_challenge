import random
import wonderwords
from wonderwords import RandomWord

# ────────────────────────────────────────────────
# Welcome
name = input("Enter Your Name: ").strip()
print(f"\nWelcome {name}!")
print("---------------")
print("Try to guess the hidden word.")
print("You have 6 lives.\n")

# ────────────────────────────────────────────────
# Word list
r = RandomWord()
word_list = [r.word(include_parts_of_speech=["nouns"]) for _ in range(120)]
word_to_be_guessed = random.choice(word_list).lower()

# Game state
secret_word = word_to_be_guessed
display = ["_"] * len(secret_word)        
guessed_letters = set()
lives = 6

# Hangman stages: 0 mistakes → 6 mistakes (7 total)
hangman_stages = [
    # 0
    """
  +---+
  |   |
      |
      |
      |
      |
========= """,
    # 1
    """
  +---+
  |   |
  O   |
      |
      |
      |
========= """,
    # 2
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
========= """,
    # 3
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= """,
    # 4
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========= """,
    # 5
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
========= """,
    # 6 (dead)
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========= """
]

# ────────────────────────────────────────────────
# Main game loop
while lives > 0 and "_" in display:
    print("\nWord:  " + " ".join(display))
    print("Lives: " + str(lives))
    print("Used:  " + ", ".join(sorted(guessed_letters)) if guessed_letters else "(none)")
    print(hangman_stages[6 - lives])   # 6 lives = stage 0, 0 lives = stage 6
    print()

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print(f"Good! '{guess}' is in the word.")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"Sorry, '{guess}' is not in the word.")

# ────────────────────────────────────────────────
# Game result
print("\n" + "="*50)
print(" ".join(display))
print(hangman_stages[6 - lives])

if "_" not in display:
    print(f"\nCONGRATULATIONS {name}! You won!")
    print(f"The word was: {secret_word}")
else:
    print(f"\nGame over... the man was hanged.")
    print(f"The word was: {secret_word}")
print("="*50)