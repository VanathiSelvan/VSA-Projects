# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random

answer = random.randint(1,9)
guess = int(raw_input("Guess a number 1 - 9! Type exit if you want to leave game: "))


if guess == "exit":
    print "GAME OVER!!"
if guess == answer:
    print "YAYY!! YOU GUESSED RIGHT"

if guess != answer:
        print "YOU'RE HORRIBLE AT THIS.JK TRY AGAIN"

if guess < answer:
    print "YOUR GUESS IS TOO LOW. GUESS HIGHER!!"
if guess > answer:
    print "YOUR GUESS IS TOO HIGH. GUESS LOWER!!"
if guess == answer:
    print "YoU ArE CoRRecT!!!! I AM SO PROUD OF YOU!!"

if guess != answer:
    print int(raw_input("Guess a number 1 - 9! Type exit if you want to leave game: "))





