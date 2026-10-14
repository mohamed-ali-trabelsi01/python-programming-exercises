def rowMult(M, i, k):
    if k == 0:
        return
    if i < 0 or i >= len(M):
        return
    for c in range(len(M[i])):
        M[i][c] *= k


def rowAdd(M, i, j, k):
    if k == 0:
        return
    if i < 0 or i >= len(M) or j < 0 or j >= len(M):
        return
    for c in range(len(M[j])):
        M[j][c] += k * M[i][c]


def reduzierteStufen(M):
    if not M or not M[0]:
        return

    rows = len(M)
    cols = len(M[0])

    for i in range(rows - 1, -1, -1):
        pivot_col = None

        for j in range(cols):
            if M[i][j] != 0:
                pivot_col = j
                break

        if pivot_col is None:
            continue

        pivot = M[i][pivot_col]
        if pivot != 1:
            rowMult(M, i, 1 / pivot)

        for k in range(i):
            if M[k][pivot_col] != 0:
                factor = -M[k][pivot_col]
                rowAdd(M, i, k, factor)
