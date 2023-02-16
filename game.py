import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):  # the underscore is an anonymous variable, in whcih we don't really care about what place we're on. (Seems odd...) 
        color = random.choice(COLORS) # we randomly select a color ...
        code.append(color)  # ... which gets appended into [code]
    return code

def guess_code():

    while True: # thsi catches things in case they input an invalid number
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors") # f strings are available in Python 3.7 and above
            continue # we break out of the for loop and it brings us back to the top of the while loop

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break # where would this put us after breaking out?
    
        else: # if you get to this point, it means that all of your colors were correct and you can break out of the while loop.
            break

    return guess  # when you've broken out of the while loop, now you can return guess

def check_code(guess, real_code):
    color_counts = {}  # how many of each color you have
    correct_pos = 0 
    incorrect_pos = 0

    for color in real_code:
        pass
