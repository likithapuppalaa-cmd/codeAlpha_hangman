import random


words = ["python", "computer", "program", "coding", "developer"]


word = random.choice(words)


guessed_letters = []


max_wrong_guesses = 6
wrong_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.\n")


while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations!")
        print("You guessed the word:", word)
        break

    
    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    
    guessed_letters.append(guess)

    
    if guess in word:
        print("✅ Correct guess!\n")
    else:
        wrong_guesses += 1
        remaining = max_wrong_guesses - wrong_guesses

        print("❌ Wrong guess!")
        print("Incorrect guesses remaining:", remaining, "\n")


else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)