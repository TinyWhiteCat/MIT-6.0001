# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True
           




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    valid_guesses = []
    for c in secret_word:
        if c in letters_guessed:
            valid_guesses.append(c)
        else:
            valid_guesses.append("_ ")
    guessed_word = ''.join(valid_guesses)
    return guessed_word    


def is_a_vowel(userinput):
    '''
    :param userinput: a single character string
    :return:  Boolean True or false.
    Checks if userinput is in the vowel list
    '''
    vowel = ['a', 'e', 'i', 'o', 'u']

    if userinput in vowel:
        return True
    else:
        return False


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    available_letters = []
    for c in alphabet:
        if c not in letters_guessed:
            available_letters.append(c)
    return ''.join(available_letters)  


def is_guess_valid(letters_guessed, userinput):
    if userinput in letters_guessed:
        valid = False
    else:
        valid = True
    return valid    


def is_guess_correct(userinput, secret_word):
    if userinput in secret_word:
        valid = True
    else:
        valid = False
    return valid


def is_guess_alpha_lower(userinput):
    return userinput.islower()


def is_guess_alpha(userinput):
    if userinput == "*":
        return True
    return userinput.isalpha() 


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = "stone"
    letters_guessed = []
    lettersNumber = 0
    guesses_left = 6
    warnings_left = 3
    
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long. ")
    print("You have", warnings_left, "warnings left")
    
    
    while guesses_left > 0:
        print("---------------")
        print("You have", guesses_left, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed))
    
        userinput = input("Please guess a letter: ")
        
        if userinput == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            guesses_left = guesses_left
            continue        
        
        if not is_guess_alpha_lower(userinput):
            userinput = userinput.lower()     
        
        if not is_guess_alpha(userinput):
            if warnings_left > 0:
                warnings_left = warnings_left - 1
                print("Oops! You've already guessed that letter. You have ", warnings_left, "warnings left.")
            else:
                guesses_left = guesses_left - 1
                print("Oops! That is not a valid letter. You have no warnings left so you loose one guess")            
        else: 
            if not is_guess_valid(letters_guessed, userinput):
                if warnings_left > 0:
                    warnings_left = warnings_left - 1
                    print("Oops! You've already guessed that letter. You have ", warnings_left, "warnings left.")
                else:
                    guesses_left = guesses_left - 1
                    print("Oops! That is not a valid letter. You have no warnings left so you loose one guess")
            else:
                if userinput in letters_guessed:
                    if warnings_left > 0:
                        warnings_left = warnings_left - 1
                        print("You have", warnings_left, "warnings left")
                    else:
                        guesses_left = guesses_left - 1
                        print('LETTER HAS ALREADY BEEN GUESSED')
                else:
                    letters_guessed.append(userinput)
                    if is_guess_correct(userinput, secret_word):
                        print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                        lettersNumber += 1
                        if is_word_guessed(secret_word, letters_guessed):
                            score = guesses_left * lettersNumber
                            print("Congratulations, you won!")
                            print("Your tatol score for this game is: ", score)
                            break
                    else:
                        print("Oops! That letter is not in my word.")
                        if is_a_vowel(userinput):
                            guesses_left = guesses_left - 2
                        else:
                            guesses_left = guesses_left - 1            
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)    
        
    

    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_cleaned = my_word.replace(' ', '')
    letters_in_my_word_cleaned = list(my_word_cleaned)
    letters_in_other_word = list(other_word)
    char_counter = len(letters_in_my_word_cleaned)
    if len(letters_in_other_word) == char_counter:
        for i in range(char_counter):
            if my_word_cleaned[i] == other_word[i]:
                continue
            elif my_word_cleaned[i] == "_" and other_word[i] not in letters_in_my_word_cleaned:
                continue
            else:
                return False
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = ""
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            possible_matches += (other_word + " ")
        else:
            continue
    if possible_matches == "":
        print("No matches found")
    else:
        print(possible_matches)





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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    guesses_left = 6
    warnings_left = 3

    print("I am thinking of a word that is ", len(secret_word), "letters long.")
    print("You have", warnings_left, "warnings left.")
    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:

        print("----------")
        print("You have ", guesses_left, "guesses left.")
        print(get_available_letters(letters_guessed))
        print(get_guessed_word(secret_word, letters_guessed))
        userinput = input("Please guess a letter: ")
        
        if userinput == "*":
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            guesses_left = guesses_left
            continue

        if not is_guess_alpha_lower(userinput):
            if warnings_left > 1:
                warnings_left = warnings_left - 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left")
            else:
                guesses_left = guesses_left - 1
                print("Oops! That is not a valid letter. You have no warnings left so you loose one guess")
        else:
            if not is_guess_valid(letters_guessed, userinput):
                if warnings_left > 1:
                    warnings_left = warnings_left - 1
                    print("Oops! You've already guessed that letter. You have ", warnings_left, "warnings left.")
                else:
                    guesses_left = guesses_left - 1
                    print("Oops! That is not a valid letter. You have no warnings left so you loose one guess")
            else:
                if is_guess_correct(userinput, secret_word):
                    letters_guessed.append(userinput)
                    print("Good Guess")
                else:
                    letters_guessed.append(userinput)
                    print("Oops! That letter is not in my word")
                if not is_guess_correct(userinput, secret_word):
                    if is_a_vowel(userinput):
                        guesses_left = guesses_left - 2
                    else:
                        guesses_left = guesses_left - 1

    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won! The word was", secret_word)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
