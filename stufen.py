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
    if len(M[i]) != len(M[j]):
        return

    for c in range(len(M[j])):
        M[j][c] += k * M[i][c]


def zeilenStufen(M):
    if not M or not M[0]:
        return

    rows = len(M)
    cols = len(M[0])

    r = 0
    c = 0
    while r < rows and c < cols:
        if M[r][c] == 0:
            for rr in range(r + 1, rows):
                if M[rr][c] != 0:
                    # Addiere die gefundene Zeile zur aktuellen
                    rowAdd(M, rr, r, 1)
                    break

        if M[r][c] == 0:
            c += 1
            continue

        for rr in range(r + 1, rows):
            if M[rr][c] != 0:
                factor = -M[rr][c] / M[r][c]
                rowAdd(M, r, rr, factor)

        pivot = M[r][c]
        rowMult(M, r, 1 / pivot)

        r += 1
        c += 1
