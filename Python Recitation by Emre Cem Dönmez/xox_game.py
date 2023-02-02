def check_board():  # Ödev
    print("")


def make_move(board, player_number, position):
    if player_number == 1:
        board[position // 3][position % 3] = "X"
    else:
        board[position // 3][position % 3] = "O"


def print_board(board):
    for i in range(len(board)):
        print("".join(board[i]))


board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

counter = 0

while True:
    print_board(board)

    # Oyunun bitip bitmediğinin kontrol edilmesi lazım.
    # Ödev

    move_position = 0
    player_number = 0
    player_name = ""

    if counter % 2 == 0:  # 1. oyuncunun sırası
        player_number = 1
        player_name = "First"
    else:  # 2. oyuncunun sırası
        player_number = 2
        player_name = "Second"
    
    move_position = int(input(f"{player_name} player: "))
    move_position -= 1
    while board[move_position // 3][move_position % 3] in ['X', 'O']:
        move_position = int(input(f"Invalid move try again. {player_name} player: "))
        move_position -= 1

    make_move(board, player_number, move_position)

    counter += 1


# connect four game
# sudoku solver