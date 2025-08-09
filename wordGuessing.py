import random

#region Method generate_random_word
def generate_random_word():
    word_list = [
        "python", "variable", "function", "iterator", "notebook",
        "pipeline", "dataset", "computer", "research", "analytics"
    ]
    return random.choice(word_list)
#endregion

#region Method make_blanks
def make_blanks(secret_word):
    return ["_" for _ in secret_word]
#endregion

#region Method play_game
def play_game(lives):
    secret_word = generate_random_word()
    word_length = len(secret_word)
    blanks = make_blanks(secret_word)
    guess_letter = set()

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {word_length} letters: {' '.join(blanks)}")

    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guess_letter:
            print("You've already guessed that letter. Try another one.")
            continue

        guess_letter.add(guess)

        if guess in secret_word:
            for i in range(word_length):
                if guess == secret_word[i]:
                    blanks[i] = guess
        else:
            lives -= 1
            print(f"Wrong! You have {lives} lives left.")

        print(' '.join(blanks))

        if "_" not in blanks:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

        if lives <= 0:
            print(f"Game Over! The word was: {secret_word}")
            break
#endregion

if __name__ == "__main__":
    lives = int(input("Please input the lives: "))
    play_game(lives)