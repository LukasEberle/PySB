import random

print("Hello, this is a mini game to demonstrate the core concept of the Binary Search Algorithm.")
print("Here are the rules: The game thinks about a number between 1 and 100(inclusive).")
print("Now you guess a number and the game tells you, if the solution is lower or higher than your number.")
print("You only have 7 guesses!")
print("The Binary Search Algorithm would need a maximum of 7 guesses, so you can win everytime, if you use it!")
print("-------------------------------------------------------------------------------------------------------")

solution = random.randint(1, 100)
num_of_tries = 1
max_tries = 7

while num_of_tries <= max_tries:
    guess = input(f"Pleas submit your guess number {num_of_tries}: ")
    guess_int = int(guess)
    if guess_int == solution:
        print("Congratulations you won!")
        break
    elif num_of_tries < max_tries and guess_int < solution:
        print("That was not correct, the solution is higher, try again!")
    elif num_of_tries < max_tries and guess_int > solution:
        print("That was not correct, the solution is lower, try again!")
    else:
        print("Sorry thar was your last attempt. If you want to win everytime check out the Binary Search Algorithm!")
    num_of_tries += 1
