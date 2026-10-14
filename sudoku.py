def isValid(board):
    # Überprüfe jede Zeile
    for row in board:
        seen = set()
        for cell in row:
            if cell != ".":
                if cell in seen:
                    return False
                seen.add(cell)

    # Überprüfe jede Spalte
    for col in range(9):
        seen = set()
        for row in range(9):
            cell = board[row][col]
            if cell != ".":
                if cell in seen:
                    return False
                seen.add(cell)

    return True
board = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]
print(isValid(board))

