'''
This module checks if board is valid

Link to GitHub: https://github.com/DariaMinieieva/puzzle_game
'''

def check_row(board: list) -> bool:
    '''
    Check if rows are valid

    >>> check_row(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
                   "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_row(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
                   "     9 5 ", " 6  63  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    for i in board:
        row = set(list(i))
        row.discard("*")
        row.discard(" ")
        i = i.replace("*", "")
        i = i.replace(" ", "")
        if len(row) != len(i):
            return False

    return True

def check_column(board: list) -> bool:
    '''
    Check if columns are valid

    >>> check_column(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
                   "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> check_column(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
                   "     9 5 ", " 6  83  *", "3      **", "  8  2***", "  2  ****"])
    True
    '''
    reverse_board = [[0 for i in range(len(board))] for j in range(len(board[0]))]

    for i, item in enumerate(board):
        for j, symbol in enumerate(item):
            reverse_board[j][i] = symbol

    for i, item in enumerate(reverse_board):
        reverse_board[i] = "".join(item)

    return check_row(reverse_board)

def check_colour_block(board: list) -> bool:
    '''
    Check if coloured blocks are valid

    >>> check_colour_block(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
                   "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> check_colour_block(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
                   "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  3  ****"])
    False
    '''
    blocks = []
    indexes = [(4,0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4)]
    k = 0

    for _ in range(5):
        temp = []
        for i in indexes:
            temp.append(board[i[0]-k][i[1]+k])
        blocks.append("".join(temp))
        k+=1

    return check_row(blocks)

def validate_board(board: list) -> bool:
    '''
    Check if board is valid

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
                   "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
                   "     9 5 ", " 6  83  *", "3      **", "  8  2***", "  2  ****"])
    True
    '''

    rows = check_row(board)
    columns = check_column(board)
    blocks = check_colour_block(board)

    if rows and columns and blocks:
        return True

    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
