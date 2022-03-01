from art import logo
import random

# constant numbers for how many guessing tries hard 10 and easy 5

HARD = 5
EASY = 10
user_attempts = EASY

# function to choose a random number between 1 to 100

def get_guessing_nbr():
    """To return a random number between 1 to 100"""
    return random.randint(1, 100)

# subtract number of guessing 
def decrease_attempts(nbr):
    nbr -= 1
    return nbr

def level_difficulity():
    # user chose a game level h or e
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == "hard":
        user_attempts = HARD
    return user_attempts

def check_guess(user_attempts,guess_nbr,user_guess_nbr):
    
    if user_guess_nbr == guess_nbr:
        print (f"You got it! The answer was {guess_nbr}.")
    elif guess_nbr < user_guess_nbr:
        print("Too high.")  
        return decrease_attempts(user_attempts)
    else: 
        print("Too low.")
        return decrease_attempts(user_attempts)


def play_game():
    # print logo game and greeting to start the game
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guess_nbr = get_guessing_nbr()
    print(f"Pssst, the correct answer is {guess_nbr}")

    user_attempts = level_difficulity()

    user_guess = 0

    while user_guess != guess_nbr:
        print(f"You have { user_attempts } attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: ")) 
        # compare the number and give a result
        user_attempts = check_guess(user_attempts,guess_nbr,user_guess)
    
        if user_attempts == 0 and user_guess != guess_nbr:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != guess_nbr:
            print("Guess again.")

play_game()



    