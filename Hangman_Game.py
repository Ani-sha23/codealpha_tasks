import random

# List of sample words
word_list = ['python', 'developer', 'hangman', 'challenge', 'code', 'programming']

# Choose a random word
word = random.choice(word_list)
guessed_letters = []
tries = 6  # Max incorrect guesses

print("Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        tries -= 1
        print(f"Wrong! Tries left: {tries}")

    # Show current progress
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print(' '.join(display_word))

    # Check win condition
    if '_' not in display_word:
        print("Congratulations! You guessed the word!")
        break
else:
    print(f"Game over! The word was: {word}")
