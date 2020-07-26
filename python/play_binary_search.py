import random


def main():
    print_tutorial()
    play_game(7)


def print_tutorial():
    print("Hello, this is a mini game to demonstrate the core concept of the Binary Search Algorithm.")
    print("Here are the rules: The game thinks about a number between 1 and 100(inclusive).")
    print("Now you guess a number and the game tells you, if the solution is lower or higher than your number.")
    print("You only have 7 guesses!")
    print("The Binary Search Algorithm would need a maximum of 7 guesses, so you can win everytime, if you use it!")
    print("-------------------------------------------------------------------------------------------------------")


def play_game(max_tries):
    solution = random.randint(1, 100)
    num_of_tries = 1
    while num_of_tries <= max_tries:
        guess = input(f"Please submit your guess number {num_of_tries}: ")
        check_guess(int(guess), solution, num_of_tries, max_tries)
        num_of_tries += 1


def check_guess(guess, solution, num_of_tries, max_tries):
    if guess == solution:
        print("Congratulations you won!")
    elif num_of_tries < max_tries and guess < solution:
        print("That was not correct, the solution is higher, try again!")
    elif num_of_tries < max_tries and guess > solution:
        print("That was not correct, the solution is lower, try again!")
    else:
        print("Sorry that was your last attempt.")
        print("If you want to win every single time check out the Binary Search Algorithm!")


if __name__ == '__main__':
    main()
