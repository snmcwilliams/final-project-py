# get word list and make random
import random
from words import word_list

# function to return word for game
def get_word():
    word = random.choice(word_list) # select random word from word list
    return word.upper() # upper for uniformity and comparison

# funcion to play the game