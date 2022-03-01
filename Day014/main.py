from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def pirnt_acount(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


print(logo)
score = 0
is_continue = True
guess = "b"
b = get_random_account()

while is_continue:
    if guess == "b":
        a = b
    b = get_random_account()

    while a == b:
        b = get_random_account()
   

    print(f"Compare A: {pirnt_acount(a)}.")
    print(vs)
    print(f"Against B: {pirnt_acount(b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(guess, a["follower_count"], b["follower_count"])

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        is_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
