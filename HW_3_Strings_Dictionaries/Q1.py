# *************** HOMEWORK 3 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
import collections


def sudoku_is_legal(board):
    """
    defaultdict means that if a key is not found in the dictionary,
    then instead of a KeyError being thrown, a new entry is created.
    The type of this new entry is given by the argument of defaultdict.

    Every element in the dictionaries is from type set (can be also list).
    When calling to cols[c] for example - if there is no such element, this element
    automatically created and then the command cols[c].add could be applied
    :param board:
    :return:
    """
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squers = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squers[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squers[(r // 3, c // 3)].add(board[r][c])
    return True


def sudoku_is_legal_without_collection(board):
    cols = [set() for i in range(9)]
    rows = [set() for i in range(9)]
    squers = [set() for i in range(9)]

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            elif board[r][c] in rows[r].union(cols[c].union(squers[(r // 3) * 3 + c // 3])):
                return False
            else:
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squers[(r // 3) * 3 + c // 3].add(board[r][c])
    return True


def sudoku_is_legal_with_lists(board):
    cols = [list() for i in range(9)]
    rows = [list() for i in range(9)]
    squers = [list() for i in range(9)]

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            elif (board[r][c] in rows[r] or
                  board[r][c] in cols[c] or
                  board[r][c] in squers[((r // 3) * 3 + c // 3)]):
                return False
            else:
                cols[c].append(board[r][c])
                rows[r].append(board[r][c])
                squers[((r // 3) * 3 + c // 3)].append(board[r][c])
    return True


legal_board1 = [
    [1, 2, 3, 4, 5, 6, 8, 7, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 5, 6, 4],
    [2, 1, 4, 3, 6, 5, 9, 8, 7],
    [3, 6, 5, 8, 9, 7, 2, 4, 1],
    [9, 7, 8, 2, 1, 4, 6, 3, 5],
    [8, 3, 1, 9, 7, 2, 4, 5, 6],
    [5, 9, 7, 6, 4, 8, 3, 1, 2],
    [6, 4, 2, 5, 3, 1, 7, 9, 8]
]

illegal_board = [
    [1, 2, 3, 4, 5, 6, 7, 9, 8],
    [4, 5, 6, 7, 8, 9, 2, 3, 1],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 1, 4, 3, 7, 5, 8, 6, 9],
    [3, 6, 7, 1, 9, 1, 5, 4, 2],
    [5, 9, 8, 2, 6, 4, 3, 1, 7],
    [8, 3, 1, 9, 4, 7, 6, 2, 5],
    [9, 7, 5, 6, 3, 2, 1, 8, 4],
    [6, 4, 2, 5, 1, 8, 9, 7, 3]
]

print(sudoku_is_legal_with_lists(board=legal_board1))
print(sudoku_is_legal_with_lists(board=illegal_board))

print(sudoku_is_legal_without_collection(board=legal_board1))
print(sudoku_is_legal_without_collection(board=illegal_board))

print(sudoku_is_legal(board=legal_board1))
print(sudoku_is_legal(board=illegal_board))
