import random


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
    rolls = ['rock', 'paper', 'scissors']
    roll1 = get_roll(player_1, rolls)
    roll2 = random.choice(rolls)
    print(f"{player_1} rolled {roll1} and {player_2} rolled {roll2}!")
    winner = find_winner(player_1, roll1, player_2, roll2)
    if winner is None:
        print("The round ended in a draw!")
    else:
        print(f"{winner} won this round!")
    return winner


def get_roll(player, rolls):
    roll = input(f"{player}, what is your roll? {rolls}: ")
    roll = roll.lower().strip()
    if roll not in rolls:
        print(f"{roll}, is not a valid option!")
        roll = get_roll(player, rolls)
    return roll


def find_winner(player_1, roll1, player_2, roll2):
    winner = None
    if roll1 == roll2:
        pass
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_2
        elif roll2 == 'scissors':
            winner = player_1
    elif roll1 == 'paper':
        if roll2 == 'scissors':
            winner = player_2
        elif roll2 == 'rock':
            winner = player_1
    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_2
        elif roll2 == 'paper':
            winner = player_1
    return winner


if __name__ == '__main__':
    main()
