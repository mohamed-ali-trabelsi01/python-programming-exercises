def isValidBlock(board):
    # Starte jede 3x3-Box (0,3,6)
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            seen = set()

            # Durchlaufe die 3x3-Zellen
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    value = board[r][c]

                    if value != ".":
                        if value in seen:
                            return False
                        seen.add(value)

    return True
