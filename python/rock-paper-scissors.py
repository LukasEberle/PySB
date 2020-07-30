import json
import random
import os
from colorama import Fore
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

rolls = {}


def main():
    print(Fore.WHITE)
    load_rolls()
    print_header()
    player = input("What's the name of Player 1? ")
    ai = "COM"
    best_of(3, player, ai)


def print_header():
    print(Fore.LIGHTMAGENTA_EX)
    print("-------------------")
    print("Rock Paper Scissors")
    print("-------------------")
    print(Fore.WHITE)


def best_of(rounds, player_1, player_2):
    list_of_results = []
    overall_winner = None
    while list_of_results.count(player_1) < int(rounds/2)+1 and list_of_results.count(player_2) < int(rounds/2)+1:
        list_of_results.append(play_game(player_1, player_2))
        print(f"The score is {player_1}: {list_of_results.count(player_1)} and {player_2}: {list_of_results.count(player_2)}")
        print("------------------------")
    if list_of_results.count(player_1):
        overall_winner = player_1
    else:
        overall_winner = player_2
    print(f"{overall_winner} won the best of {rounds} match!")


def play_game(player_1, player_2):
    roll_names = list(rolls.keys())
    roll1 = get_roll(player_1, roll_names)
    roll2 = random.choice(roll_names)
    print(f"{player_1} rolled " + Fore.GREEN + f"{roll1}")
    print(Fore.WHITE + f"and {player_2} rolled " + Fore.GREEN + f"{roll2}" + Fore.WHITE + "!")
    print(Fore.WHITE)
    winner = find_winner(player_1, roll1, player_2, roll2)
    if winner is None:
        print(Fore.YELLOW + "The round ended in a draw!")
        print(Fore.WHITE)
    else:
        print(Fore.YELLOW + f"{winner} won this round!")
        print(Fore.WHITE)
    return winner


def get_roll(player, roll_names):
    print(f"Rolls available: {', '.join(roll_names)}.")
    if os.environ.get('PYCHARM_HOSTED') == "1":
        print(Fore.LIGHTRED_EX + "Warning: Some Features are not available, when run in PyCharm")
        roll = input(Fore.WHITE + f"{player}, what is your roll: ")
    else:
        word_comp = WordCompleter(roll_names)
        roll = prompt(f"{player}, what is your roll: ", completer=word_comp)
    roll = roll.lower().strip()
    if roll not in roll_names:
        print(Fore.LIGHTRED_EX + f"{roll}, is not a valid option!")
        print(Fore.WHITE)
        roll = get_roll(player, roll_names)
    return roll


def find_winner(player_1, roll1, player_2, roll2):
    if roll1 == roll2:
        return None
    outcome = rolls.get(roll1)
    if roll2 in outcome.get('defeats'):
        return player_1
    if roll2 in outcome.get('defeated_by'):
        return player_2


def load_rolls():
    global rolls
    filename = '../data/rps-rules.json'
    with open(filename, 'r', encoding='utf-8') as data:
        rolls = json.load(data)


if __name__ == '__main__':
    main()
