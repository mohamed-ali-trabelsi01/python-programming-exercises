def rowMult(M, i, k):
    """Multipliziert die i-te Zeile der Matrix M mit dem Faktor k."""

    if not isinstance(M, list) or i < 0 or i >= len(M):
        return

    if k == 0:
        return

    for col in range(len(M[i])):
        M[i][col] *= k


def rowAdd(M, i, j, k):
    """Addiert das k-fache der i-ten Zeile zur j-ten Zeile der Matrix M."""

    if (
        not isinstance(M, list)
        or i < 0 or i >= len(M)
        or j < 0 or j >= len(M)
    ):
        return

    # Falls k = 0, Matrix nicht verändern
    if k == 0:
        return

    if len(M[i]) != len(M[j]):
        return
    for col in range(len(M[j])):
        M[j][col] += k * M[i][col]
