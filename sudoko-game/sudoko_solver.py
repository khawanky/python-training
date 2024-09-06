test_board = [
    [7, 0, 2, 0, 5, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [1, 0, 0, 0, 0, 9, 5, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 4, 3, 0, 0, 0, 7, 5, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 9, 7, 0, 0, 0, 0, 5],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 4, 0, 2, 0, 3]
]

GRID_SIZE = 9


def get_board_from_user():
    user_board = []
    for row in range(GRID_SIZE):
        user_board_row = input(f"Please put all your board numbers row {row}\n")
        temp_row = []
        for row_item in range(GRID_SIZE):
            temp_row.append(int(user_board_row[row_item]))
        user_board.append(temp_row)
    return user_board

def print_board(board):
    for x in range(GRID_SIZE):
        if x%3==0 and x!=0:
            print("-----------")
        for y in range(GRID_SIZE):
            if y%3==0 and y!=0:
                print("|", end="")
            print(board[x][y], end="")
        print('')

def is_num_in_row(board, num, row):
    for item in range(GRID_SIZE):
        if board[row][item] == num:
            return True
    return False

def is_num_in_col(board, num, col):
    for item in range(GRID_SIZE):
        if board[item][col] == num:
            return True
    return False

def is_num_in_box(board, num, row, col):
    local_box_row = row - row%3
    local_box_col = col - col%3
    for x in range(local_box_row, local_box_row+3):
        for y in range(local_box_col, local_box_col+3):
            if board[x][y] == num:
                return True
    return False

def is_valid_placement(board, num, row, col):
    return (not is_num_in_row(board, num, row)
            and not is_num_in_col(board, num, col)
            and not is_num_in_box(board, num, row, col))

def solve_board(board):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if board[x][y] == 0:
                for num_to_try in range(1,GRID_SIZE+1):
                    if is_valid_placement(board, num_to_try, x, y):
                        board[x][y] = num_to_try
                        if solve_board(board):
                            return True
                        else:
                            board[x][y] = 0
                return False
    return True

def main(from_user):
    board_to_solve = test_board
    if from_user:
        board_to_solve = get_board_from_user()
    print_board(board_to_solve)
    if solve_board(board_to_solve):
        print("\nBoard solved!\n")
        print_board(board_to_solve)
    else:
        print("\nBoard can't be solved!\n")

main(True)



