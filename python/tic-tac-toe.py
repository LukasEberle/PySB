

def main():
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ["X", "O"]
    while not check_winner(board):
        player = players[active_player_index]
        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbols[active_player_index]):
            print("That's not a valid option!")
            continue
        active_player_index = (active_player_index + 1) % len(players)

    print(f"{player} won with this board: ")
    show_board(board)


def announce_turn(player):
    print()
    print(f"{player} can make a symbol!")
    print()


def check_winner(board):
    sequences = get_winning_sequences(board)
    for cells in sequences:
        symbol = cells[0]
        if symbol and all(symbol == cell for cell in sequences):
            return True
    return False


def get_winning_sequences(board):
    sequences = []
    rows = board
    sequences.extend(rows)
    for i in range(0, 3):
        col = [
            board[0][i],
            board[1][i],
            board[2][i]
        ]
        sequences.append(col)
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    sequences.extend(diagonals)
    return sequences


def show_board(board):
    for row in board:
        print("| ", end='')
        for cell in row:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()


def choose_location(board, symbol):
    row = int(input("Choose which row: "))
    column = int(input("Choose which column: "))
    row -= 1
    column -= 1
    if row < 0 or row >= len(board):
        return False
    if column < 0 or column >= len(board[0]):
        return False
    cell = board[row][column]
    if cell is not  None:
        return False
    board[row][column] = symbol
    return True


if __name__ == '__main__':
    main()
