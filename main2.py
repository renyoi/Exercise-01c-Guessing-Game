#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
number1 = random.randrange(1,11)
number2 = random.randrange(1,11)
number3 = random.randrange(1,11)
number4 = random.randrange(1,11)
number5 = random.randrange(1,11)
while True:
    try:
        guess = int(input("Guess a number from 1 to 10: "))
    except ValueError:
        print("That's not a number. Learn to follow instructions.")
        continue
    else:
        break
if guess == number1:
    print("Great job! You got it!")
    while True:
        try:
            guess = int(input("Let's see if you can get 5 in a row. Enter another number!"))
        except ValueError:
            print("That's not a number. Try again, and learn to follow instructions.")
            continue
        else:
            break
    if guess == number2:
        print("Right again!")
        while True:
            try:
                guess = int(input("Let's keep going! Pick another number."))
            except ValueError:
                print("That's not a number. Try again, and learn to follow instructions.")
                continue
            else:
                break
        if guess == number3:
            print("Yes! You're on a roll!")
            while True:
                try:
                    guess = int(input("Just 2 more! You can do it! Pick a number."))
                except ValueError:
                    print("That's not a number. Try again, and learn to follow instructions.")
                    continue
                else:
                    break
            if guess == number4:
                print("Correct!")
                while True:
                    try:
                        guess = int(input("Only one left! Here we go!"))
                    except ValueError:
                        print("That's not a number. Try again, and learn to follow instructions.")
                        continue
                    else:
                        break
                if guess == number5:
                    print("YES! You got all 5 right! Congratulations!")
                else:
                    print("Incorrect! And you were so close, too...")
                    print("The number was " + str(number5))
            else:
                print("Sorry, better luck next time.")
                print("The number was " + str(number4))
        else: 
            print("Sorry, better luck next time.")
            print("The number was " + str(number3))
    else:
        print("Sorry, better luck next time.")
        print("The number was " + str(number2))
else:
    print("Sorry, better luck next time.")
    print("The number was " + str(number1))