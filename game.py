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
            continue # brings us back to the top of the while loop (NOT the if statement)

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break # where would this put us after breaking out?