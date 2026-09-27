import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Choose a random word
word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Maximum number of incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.\n")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with underscores
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    # Get a letter from the user
    guess = input("Enter a letter: ").lower()

    # Check whether the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    # Add the guessed letter to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("✅ Correct guess!\n")
    else:
        wrong_guesses += 1
        remaining = max_wrong_guesses - wrong_guesses

        print("❌ Wrong guess!")
        print("Incorrect guesses remaining:", remaining, "\n")

# If the player uses all 6 incorrect guesses
else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)