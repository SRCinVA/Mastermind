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
        if color not in color_counts: # if the key (the color) is not in the dictionary ...
            color_counts[color] = 0 # ... then we want to add it. Apparently you do this in the first position
        color_counts[color] += 1    # don't understand the rationale behind this line ...

    # to deal with the correct colors
    for guess_color, real_color in zip(guess, real_code): # zip() wil create a handy tuple showing us the correct and the guessed item next to each other.
        if guess_color == real_color:                     # the for loop decomposes that tuple.
            correct_pos += 1                              # here, you record the number of correct items
            color_counts[guess_color] -= 1                # then, we have to subtract that away so that we don't count it as incorrect. This removes it from consideration.

    # next, to deal with the incorrect colors
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:  # meaning, (1.) if there's a key and (2.) there's still a color left in the list
            incorrect_pos += 1
            color_counts[guess_color] -= 1               # like above, we have to clear this one from the list

    return correct_pos, incorrect_pos

def game():
    
    print(f"Welcome to Mastermind--you have {TRIES} to guess the code...")

    code = generate_code()
    for attempts in range(1, TRIES + 1): # + to make sure it covers the complete set (1 to 10, inclusive)
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break # this cuts off the function right here, as they got everything correct.

        print(f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")

    else:
        print("You ran out of tries; the code was: ", *code)  # *code will print out every individual element from 'code', separated by spaces.
