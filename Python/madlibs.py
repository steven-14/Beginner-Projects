# This is my beginner project,  code along with Kylie Ying.
# Youtube video: 12 Beginner Python Projects - Coding Course - FreeCodeCamp.org
# Guess a number - computer

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        #print(guess) #check
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number: # this part is not running.
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guess the number {random_number}')
    
guess(10)    
