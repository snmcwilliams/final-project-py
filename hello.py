# get word list and make random
import random
from words import word_list

# select word for game
def get_word():
    word = random.choice(word_list)
    return word.upper() # upper for uniformity and comparison

# play the game
def gameplay(word):
    word_selected = "_" * len(word) # place holder for each letter
    guessed = False
    guessed_letters = [] # stores letters guessed
    guessed_words = [] # stores words guessed
    attempts = 6
    print("Let's play!")
    print(display_hangman(attempts)) # show initial stage
    print(word_selected) # show word/underscores to guess
    print("\n")
# run until word is guessed or runs out of attempts
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
 # conditions for guessing letter - duplicate, not found and is found.
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Oops, you've already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word. Sorry.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Well done, ", guess, " is in the word!")
                guessed_letters.append(guess)
# display guess occurrences
                word_as_list = list(word_selected) # string to list for index
            # find indices where guess occurs in word
                indices = [i for i, letter in enumerate(word) if letter == guess] # get index and letter at index for each iteration
            # replace underscore at index with guess
                for index in indices:
                    word_as_list[index] = guess
                word_selected = "".join(word_as_list) # list to string
                if "_" not in word_selected:
                    guessed = True
# conditions for guessing word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Oops, you've already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word. Sorry.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_selection = word
# conditions for guessing other
        else:
            print("Invalid guess.")
    # show after each attempt
        print(display_hangman(attempts))
        print(word_selected)
        print("\n")
    if guessed:
        print("Awesome, you guessed the word!")
    else:
        print("Darn it, you've exceeded number of attempts. The word was "+ word + ". Try Again!")




def display_hangman(attempts):
    stages = [
        """
            ---------
            |       |
            |       O
            |      \\|/
            |       |
            |      / \\
            ---
        """,
        """
            ---------
            |       |
            |       O
            |      \\|/
            |       |
            |      /
            ---
        """,
        """
            ---------
            |       |
            |       O
            |      \\|
            |       |
            |
            ---
        """,
        """
            ---------
            |       |
            |       O
            |       |
            |       |
            |
            ---
        """,
        """
            ---------
            |       |
            |       O
            |
            |
            |
            ---
        """,
        """
            ---------
            |       |
            |
            |
            |
            |
            ---
        """
    ]
    return stages[attempts]