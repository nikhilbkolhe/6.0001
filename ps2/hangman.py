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
import os

WORDLIST_FILENAME = "/ps2/words.txt" #nikhil Change


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    print(os.getcwd()) # nikhil Change
    inFile = open(os.getcwd() + WORDLIST_FILENAME, 'r') #nikhil Change
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
    isGuessed = True
    for letter in secret_word:
      if (letter not in letters_guessed):
        isGuessed = False
        break      
    return isGuessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    lettersGuessed = ""
    for letter in secret_word:
      if (letter in letters_guessed):
        lettersGuessed += letter
      else:
        lettersGuessed += "_ "
    return lettersGuessed



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    availableLetters = string.ascii_lowercase
    for letter in letters_guessed:
      availableLetters = availableLetters.replace(letter, "")
    return availableLetters
    

def calculate_score(secret_word,guess_count):
  """
    secret_word: string, word which is to be guessed

    guess_count: int, number of guesses remaining

    returns : int, score calculated as (no. of unique letters in secret word) * n. of remaining guesses
  """
  unique_letters = ""
  for letter in secret_word:
    if letter not in unique_letters:
      unique_letters += letter
    else:
      continue
  return len(unique_letters) * guess_count


def is_game_over(secret_word,letters_guessed,guess_count):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    guess_count: int, number of guessses remaining
    returns: boolean, if the game has reached its end or not
    '''
    is_game_over = False
    if(is_word_guessed(secret_word, letters_guessed)):
      print("Congratulations, You won!")
      print("Your total scrore for this game is:",calculate_score(secret_word, guess_count))
      is_game_over = True
    elif(guess_count < 1):
      is_game_over = True
      print("Sorry, you ran out of guesses. The word was:",secret_word)
    return is_game_over

#-------------------------------------------------------------------------------------------------------------------------------

def validate_input(raw_input,warnings_count,guess_count,secret_word,letters_guessed,hint = False):
  """
    raw_input: string, guess entered by user

    warnings_count: int, number if warnings remaining for the game

    guess_count: int, number of guesses remaining for the game

    secret_word: string, word which is to be guessed

    letters_guessed: list, guesses made until now

    hint: boolean, hint mode activated or not. Default is False (optional, named)

    returns: a tuple containing -
                      1. boolean: True if input passes all validations
                      2. string: lowercased and stripped version of guess
                      3. int: remaining warnings after validating current guess
                      4. int: number of remaining guesses after validating current guess

    This function performs validations on guess currently made and prints correct validation messages

    * reduce a warning if guess is not alphabets

    * if hint mode is active asterisk '*' is allowed as guess

    * reduce a warning if a guess is repeated

    * if all warnings are over reduce a guess

    * clean guess by converting to lower and stripping extra spaces
  """
  is_input_valid = True
  validated_input = ""

  # validate input againts non alpha characters
  if not (raw_input.isalpha()):

    # "*" is allowed only when hint is active
    if not (hint and raw_input == "*"):
      is_input_valid = False
      print("Oops! that is not a valid letter.",end='')

    # hints are available after guessing atleast 1 letter
    elif not (hint and raw_input == "*" and len(letters_guessed) > 0):
      is_input_valid = False
      print("Hints are available after guessing atleast 1 letter")      
    else:
      validated_input = raw_input


  # same character should not be inputted twice
  elif (raw_input.lower() in letters_guessed):
    is_input_valid = False
    print("Oops! You've already guessed that letter.",end='')
  else:
      validated_input = raw_input.lower().strip()


  # deduct warnings and guesses
  if not (is_input_valid):
    if (warnings_count < 1):
      guess_count -= 1
      print("You have no warnings left so you loose 1 guess:", get_guessed_word(secret_word, letters_guessed))
    else :
      warnings_count -= 1
      print("You have",warnings_count,"warnings left:", get_guessed_word(secret_word, letters_guessed))
  
  # return tuple so that it could be unpacked and update correct guess and warning counts
  return (is_input_valid,validated_input,warnings_count,guess_count)


#----------------------------------------------------------------------------------------------------------------------------


def process_input(guess,secret_word,letters_guessed,guess_count):
  """
    guess: string, valiadated and cleaned guess entered by user

    secret_word: string, word which is to be guessed

    letters_guessed: list, guesses made until now
    
    guess_count: int, number of guesses remaining for the game

    returns: int, remaining number of guesses

    This function checks if guessed letter is in the word to be guessed

    * if guess is a vowel and not in secret_word reduce 2 guesses

    * if guess is a consonant and not is secret_word reduce 1 guess
  """
  vowels = ['a','e','i','o','u']
  if guess in secret_word:
    print("Good guess:",get_guessed_word(secret_word, letters_guessed))
  else:
    if (guess in vowels):
      guess_count -= 2
    else:
      guess_count -= 1
    print("Oops! thats not a letter in my word:",get_guessed_word(secret_word, letters_guessed))
  return guess_count

#-------------------------------------------------------------------------------------------------------
# moved these function before hangman in order to reuse code
def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
             corresponding letters of other_word, or the letter is the special symbol
             _ , and my_word and other_word are of the same length;
             False otherwise: 
    '''
    my_word_stripped = my_word.strip(" ")
    my_word_stripped = my_word_stripped.replace(" ","")
    unique_letters = set(my_word_stripped)
    unique_letters.discard("_")
    is_match_with_gaps = True
    
    # return Flase if lengths dont match
    if not (len(my_word_stripped) == len(other_word)):
      is_match_with_gaps = False
      return is_match_with_gaps

    # for every unique letter in currently guessed word. check if all 
    # appearances of the letter are present at all the same indices in currently guessed word and 
    # some word from words_list. if any of the indices do not match, move to next word. 
    for letter in unique_letters:
      index_my_word = 0
      index_other_word = 0
      while (index_my_word != -1):          
        index_my_word = my_word_stripped.find(letter,index_my_word,len(my_word_stripped))
        if (index_my_word != -1):            
          index_other_word = other_word.find(letter,index_other_word,len(other_word))            
          if (index_my_word != index_other_word):
            is_match_with_gaps = False
            return is_match_with_gaps            
          else:
            index_my_word += 1                                      # to search for next appearance of the letter in currently guessed word
            index_other_word += 1                                   #  to search for next appearance of the letter

    return is_match_with_gaps    

# ----------------------------------------------------------------------------------------------------------------------------------------------

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = ""
    for word in wordlist:
      if(match_with_gaps(my_word, word)):
        possible_matches += " " + word
    if (len(possible_matches) > 0):
      print (possible_matches)
    else:
      print ("No Match found")




def process_input_hints (guess,secret_word,letters_guessed,guess_count):
  """
    guess: string, valiadated and cleaned guess entered by user

    secret_word: string, word which is to be guessed

    letters_guessed: list, guesses made until now
    
    guess_count: int, number of guesses remaining for the game

    returns: int, remaining number of guesses

    This function hooks to process guesses of hints are ON.

    * if guess is '*' then print all possible words based on currently guessed word

    * Otherwise call the normal process_input fnction

  """

  if (guess == "*"):
    print("Possible Matches are:")
    show_possible_matches(get_guessed_word(secret_word, letters_guessed))
  else:
    guess_count = process_input(guess, secret_word, letters_guessed, guess_count)
  return guess_count



def hangman(secret_word,hint = False):
    '''
    secret_word: string, the secret word to guess.

    hint: boolean, hint mode activated or not. Default is False (optional, named)
    
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
    
    # initialization
    warnings_count = 3
    guess_count = 6
    letters_guessed = []
    print("Welcome the game Hangman!")
    print("I am thinking of a word that is", len(secret_word),"letters long")
    print("You have",warnings_count,"warnings left.")
    
    # continue the game until word is guessed or guesses are over
    while not (is_game_over(secret_word,letters_guessed,guess_count)):
      print("-------------------------------------------")
      print("You have",guess_count,"guesses left")
      print("Available letters:",get_available_letters(letters_guessed))
      raw_input = input("Please guess a letter: ")
      
      # validate raw input and convert to lowercase, optional parameter hint= to accept "*" as input
      (is_input_valid,validated_input,warnings_count,guess_count) = validate_input(raw_input,warnings_count,guess_count,secret_word,letters_guessed,hint=hint)
      if(is_input_valid):
        letters_guessed.append(validated_input)

        # check if guess is correct, updates guess and loop away
        if (hint):          
          guess_count = process_input_hints(validated_input, secret_word, letters_guessed, guess_count)
        else:
          guess_count = process_input(validated_input,secret_word,letters_guessed,guess_count)        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



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
    
    # added a hint optional parameter to hangman function to call code which processes hints
    hangman(secret_word,hint = True)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    secret_word = "else"
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
#    secret_word = "ample"
    hangman_with_hints(secret_word)
