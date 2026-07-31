import random

# List of predefined words
words = ["python", "apple", "orange", "laptop", "coding"]

# Select random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Wrong guesses allowed
wrong_guesses = 0
max_wrong = 6

print("=" * 40)
print("WELCOME TO HANGMAN")
print("=" * 40)

while wrong_guesses < max_wrong:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("Correct Word was:", secret_word)