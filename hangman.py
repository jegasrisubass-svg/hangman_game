import random

# 1. List of predefined words
words = ["apple", "tiger", "python", "school", "computer"]

# 2. Choose a random word
word = random.choice(words)

# 3. Create blanks
guessed_word = ["_"] * len(word)

# 4. Maximum incorrect guesses
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

# 5. Game loop
while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/ 6")

    guess = input("Enter a letter: ").lower()

    # 6. Check the guess
    if guess in word:
        print("Correct! ✅")

        # Show the correct letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong! ❌")

# 7. Check win or lose
if "_" not in guessed_word:
    print("\n🎉 You Win!")
    print("The word was:", word)

else:
    print("\n💀 Game Over!")
    print("The word was:", word)