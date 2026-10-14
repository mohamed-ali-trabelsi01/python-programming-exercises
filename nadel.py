# nadel.py

def str_index(heuhaufen, nadel):
    n = len(heuhaufen)
    m = len(nadel)

    if m > n:
        return -1

    for i in range(n - m + 1):
        found = True
        for j in range(m):
            if heuhaufen[i + j] != nadel[j]:
                found = False
                break
        if found:
            return i
    return -1


print(str_index("sadbutsad", "sad"))
print(str_index("leetcode", "leeto"))
print(str_index("mississippi", "issip"))
print(str_index("abc", ""))
print(str_index("abc", "abc"))
