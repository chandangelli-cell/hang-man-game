import random

# Predefined list of words
words = ["python", "coding", "hangman", "computer", "program","java","portofolio","developer","chatbot"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    # Display word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    # Check win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

# Lose condition
if attempts == 0:
    print("\n❌ Game Over! The word was:", word)
