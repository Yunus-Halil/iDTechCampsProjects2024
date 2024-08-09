import random


def hangman():
    words = [
        "sidthekid", "bman", "cybertruck", "bodywash", "clothing",
        "computer", "python", "program", "glasses", "sweatshirt",
        "sweatpants", "mattress", "friends", "clocks", "biology",
        "algebra", "suitcase", "knives", "ninjas", "shampoo"
    ]

    # Randomly choose a word from the list
    chosen_word = 'hello'

    guessed_letters = []
    guess_word = ['-' for _ in chosen_word]

    HANGMAN = [
        """
        -----
        |   |
        |
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        |  -+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  |
        |
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | 
        |
        --------
        """,
        """
        -----
        |   |
        |   0
        | /-+-\ 
        |   | 
        |   | 
        |  | | 
        |  | | 
        |
        --------
        """]

    attempts = 0
    max_attempts = len(HANGMAN) - 1

    while '-' in guess_word and attempts < max_attempts:
        print(HANGMAN[attempts])
        print('Current word: ', ' '.join(guess_word))

        # Prompt the user for input
        user_guess = input("Guess a letter or the whole word: ").lower()

        if len(user_guess) == 1:
            if user_guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(user_guess)

            if user_guess in chosen_word:
                # Update the guess_word list with the correct guess
                for index in range(len(chosen_word)):
                    if user_guess == chosen_word[index]:
                        guess_word[index] = user_guess
            else:
                # Increment attempts if the guess is incorrect
                attempts += 1
        elif len(user_guess) == len(chosen_word):
            if user_guess == chosen_word:
                guess_word = list(chosen_word)
                break
            else:
                print("Incorrect guess.")
                attempts += 1
        else:
            print("Invalid input. Please guess a single letter or the whole word.")

    if '-' not in guess_word:
        print("Congratulations! You've guessed the word:", chosen_word)
    else:
        print(HANGMAN[attempts])
        print("Game over. The word was:", chosen_word)


hangman()
