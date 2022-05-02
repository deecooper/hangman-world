import random
def get_word():
    """
    This function gets the random word from the words.txt file"""
    with open("words.txt", "r") as f:
        word = f.readlines()
    word_choice = random.choice(word)
    return word_choice
    



game = get_word()
print(game)

def hangman_word(word_choice):
    #https://www.youtube.com/watch?v=m4nEnsavl6w
    """
    This function return the word as underscores for the user to guess the word
    """
    word_completion = "_" + len(word_choice)
    guessed = False
    letters_guessed = []
    words_guessed = []
    tries = 8
    print(tries)
    print(word_completion)

hangman = hangman_word(word_choice)
print(hangman)