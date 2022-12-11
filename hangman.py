# Problem Set 2, hangman.py
# Name: Brandon Kongwe
# Collaborators:
# Time spent: 11/10/2021 - 14/10/2021 (4 days)

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code


# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    gword = ""
    for char in secret_word:
        gword += (char if char in letters_guessed else "_ ")
    return gword


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    all_letters = string.ascii_lowercase
    available_letters = ""

    for char in all_letters:
        if char not in letters_guessed:
            available_letters += char
    return available_letters


# function for new guesses
def new_guess(letters_guessed, guesses_remaining):
    print("--------------------------")
    print("You have {} guesses left.".format(guesses_remaining))
    print("Available letters: {}".format(get_available_letters(letters_guessed)))
    return str.lower(input("Please guess a letter: "))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))

    letters_guessed = []  # list where guessed letters will be appended to

    guesses_remaining = 6

    warnings_remaining = 3

    vowels = ["a", "e", "i", "o", "u"]

    print("You have {} warnings left".format(warnings_remaining))

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        new_letter = new_guess(letters_guessed, guesses_remaining)
        # checking if user entered anything besides an alphabet
        if warnings_remaining > 0 and not new_letter.isalpha():
            warnings_remaining -= 1
            print("Oops! That is not a valid letter. You have {} warnings left.".format(warnings_remaining),
                  get_guessed_word(secret_word, letters_guessed))
        elif warnings_remaining == 0 and not new_letter.isalpha():
            guesses_remaining -= 1
            print("Oops! That is not a valid letter. You have {} guesses left.".format(guesses_remaining),
                  get_guessed_word(secret_word, letters_guessed))
        # if user entered an already guessed word, they lose one warning
        elif new_letter in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have {} warnings left".format(warnings_remaining),
                      get_guessed_word(secret_word, letters_guessed))
            # if no warnings left, user loses one guess
            elif warnings_remaining == 0 and guesses_remaining > 0:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have {} guesses left".format(guesses_remaining),
                      get_guessed_word(secret_word, letters_guessed))
        elif new_letter not in secret_word:
            # if user guesses a vowel not already guessed or in the secret word, they lose 2 guesses
            if new_letter in vowels:
                guesses_remaining -= 2
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                # if user guesses a consonant not already guessed or in the secret word, they lose 1 guess
                guesses_remaining -= 1
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
        else:
            new_letter = new_letter.lower()
            letters_guessed.append(new_letter)
            # if user guesses a correct letter
            if new_letter in secret_word:
                print("Good guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                # if user guesses a wrong letter
                guesses_remaining -= 1
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))

    print("-------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
        # set does not allow duplicates. able to get unique values
        total_score = guesses_remaining * len(set(secret_word))
        print("Congratulations, you won!")
        print("Your total score for this game is: {}".format(total_score))
    else:
        print("Sorry, you ran out of guesses. The word was {}".format(secret_word))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''

    stripped = my_word.replace(" ", "")
    letters = ""
    if len(stripped) != len(other_word):
        return False
    for index in range(len(stripped)):
        if stripped[index] != "_":
            if stripped[index] != other_word[index]:
                return False
            letters = letters + other_word[index]
        else:
            if other_word[index] in letters:
                return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    match = ""
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match += word
            match += " "
    if match != "":
        print(match)
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long".format(len(secret_word)))

    letters_guessed = []  # list where guessed letters will be appended to

    guesses_remaining = 6

    warnings_remaining = 3

    vowels = ["a", "e", "i", "o", "u"]

    print("You have {} warnings left".format(warnings_remaining))

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        new_letter = new_guess(letters_guessed, guesses_remaining)
        # allowing user to guess with asterisk (*)
        if new_letter == "*":
            print("Possible word matches are: ")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        # checking if user entered anything besides an alphabet
        elif warnings_remaining > 0 and not new_letter.isalpha():
            warnings_remaining -= 1
            print("Oops! That is not a valid letter. You have {} warnings left.".format(warnings_remaining),
                  get_guessed_word(secret_word, letters_guessed))
        elif warnings_remaining == 0 and not new_letter.isalpha():
            guesses_remaining -= 1
            print("Oops! That is not a valid letter. You have {} guesses left.".format(guesses_remaining),
                  get_guessed_word(secret_word, letters_guessed))
        # if user entered an already guessed word, they lose one warning
        elif new_letter in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have {} warnings left".format(warnings_remaining),
                      get_guessed_word(secret_word, letters_guessed))
            # if no warnings left, user loses one guess
            elif warnings_remaining == 0 and guesses_remaining > 0:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have {} guesses left".format(guesses_remaining),
                      get_guessed_word(secret_word, letters_guessed))
        elif new_letter not in secret_word:
            # if user guesses a vowel not already guessed or in the secret word, they lose 2 guesses
            if new_letter in vowels:
                guesses_remaining -= 2
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                # if user guesses a consonant not already guessed or in the secret word, they lose 1 guess
                guesses_remaining -= 1
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))
        else:
            new_letter = new_letter.lower()
            letters_guessed.append(new_letter)
            # if user guesses a correct letter
            if new_letter in secret_word:
                print("Good guess: {}".format(get_guessed_word(secret_word, letters_guessed)))
            else:
                # if user guesses a wrong letter
                guesses_remaining -= 1
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed)))

    print("-------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
        # set does not allow duplicates. able to get unique values
        total_score = guesses_remaining * len(set(secret_word))
        print("Congratulations, you won!")
        print("Your total score for this game is: {}".format(total_score))
    else:
        print("Sorry, you ran out of guesses. The word was {}".format(secret_word))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
