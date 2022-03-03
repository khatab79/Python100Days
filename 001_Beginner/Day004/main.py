import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# Role of the game :
#   - Rock wins against scissors.
#   - Scissors win against paper.
#   - Paper wins against rock.

# generate a random choice for the computer and store it.
computer = random.randint(0,2)

# img icons for the game
# 0 for Rock, 1 for Paper or 2 for Scissors.
gameIcons = [rock, paper, scissors] 

# store the user's input.
user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# control the user entry. Only digit
if user.isdigit() == True:
    user = int(user)
else:
    # catch user's error 
    user = -999

if(user >= 0) and (user <=2):
    # print the icons for computer and user 
    print(gameIcons[user])
    print("\n Computer chose:\n")
    print(gameIcons[computer])

    if(user == computer):
        gameResults = "It is a draw"
    
    elif(computer == 0) and (user != 1 ):
        # Paper wins against rock.
        gameResults = "You lose"

    elif(computer == 1) and (user != 2 ):
        # Scissors win against paper.
        gameResults = "You lose"

    elif(computer == 2) and (user != 0):
        # Rock wins against scissors.
        gameResults = "You lose"

    else:
        gameResults = "You win"
else:
    # wrong user entry
    gameResults = "ohh no! you lose. try again and choose 0, 1, 2"

# shows the games result
print(gameResults)


