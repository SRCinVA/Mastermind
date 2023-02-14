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
    guess = input("Guess: ").upper().split(" ")

