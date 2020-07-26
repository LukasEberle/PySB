import random

rolls = {
    'rock': {
        'defeats': ['scissors', 'sponge'],
        'defeated_by': ['paper', 'well']
    },
    'paper': {
        'defeats': ['rock', 'well'],
        'defeated_by': ['scissors', 'sponge']
    },
    'scissors': {
        'defeats': ['paper', 'sponge'],
        'defeated_by': ['rock', 'well']
    },
    'well': {
        'defeats': ['rock', 'scissors'],
        'defeated_by': ['paper', 'sponge']
    },
    'sponge': {
        'defeats': ['paper', 'well'],
        'defeated_by': ['rock', 'scissors']
    }
}


def main():
    print_header()
    player = input("What's the name of Player 1? ")
    ai = "COM"
    best_of(3, player, ai)


def print_header():
    print("-------------------")
    print("Rock Paper Scissors")
    print("-------------------")


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
    print(f"{player_1} rolled {roll1} and {player_2} rolled {roll2}!")
    winner = find_winner(player_1, roll1, player_2, roll2)
    if winner is None:
        print("The round ended in a draw!")
    else:
        print(f"{winner} won this round!")
    return winner


def get_roll(player, roll_names):
    roll = input(f"{player}, what is your roll? {roll_names}: ")
    roll = roll.lower().strip()
    if roll not in roll_names:
        print(f"{roll}, is not a valid option!")
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


if __name__ == '__main__':
    main()
