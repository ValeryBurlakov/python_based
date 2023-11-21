import random


def generate_boards():
    board_list = []

    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
                    board[i] + i == col + row or \
                    board[i] - i == col - row:
                return False
        return True

    def backtrack(board, row, result):
        if row == n:
            result.append(tuple(board))
            return

        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1, result)
                board[row] = -1  # reset

    n = 8  # size of the board
    board = [-1] * n
    result = []

    backtrack(board, 0, result)

    filtered_results = []
    for res in result:
        if sum(res) % 2 == 0:
            filtered_results.append(res)

    for res in filtered_results[:4]:
        coordinates = [(i + 1, res[i] + 1) for i in range(n)]
        random.shuffle(coordinates)  # Shuffle the coordinates randomly
        board_list.append(coordinates)
    return board_list
# generate_boards()
# print(board_list)
# print(generate_boards())