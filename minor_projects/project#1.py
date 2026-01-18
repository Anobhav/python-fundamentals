#Snake, water gun game using python 
import random

lista=["snake", "water", " Gun "]
def random_generator(lista):
    computer_choice=random.choice(lista)
    print(f"Computer choice: {computer_choice}")
    return computer_choice.lower().strip()

def user_input():
    user_choice=(input("Please enter what would you like to select? \n 1) Snake 2) Water 3) GUN\n"))
    print(f"user choice: {user_choice}")
    return user_choice.lower().strip()

def winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        print("its a tie no one wins")
    elif user_choice=="snake" and computer_choice=="water" or user_choice=="water" and computer_choice=="gun" or user_choice=="gun" and computer_choice=="snake":
        print("user wins")
    else:
        print("computer wins")
user_choice=user_input()
computer_choice=random_generator(lista)
winner(user_choice, computer_choice)
