import random

def is_sorted(lst):
    """
    Prüft, ob die Liste aufsteigend sortiert ist.
    """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def bogo_sort(lst):
    """
    Sortiert die Liste mittels Bogo-Sort.
    Mischt die Liste zufällig so lange,
    bis sie sortiert ist.
    """
    while not is_sorted(lst):
        random.shuffle(lst)
    return lst



print(bogo_sort([3, 2, 1]))       # -> [1, 2, 3]
print(bogo_sort([1, 2, 3]))       # -> [1, 2, 3]
print(bogo_sort([3, 1, 3, 2]))    # -> [1, 2, 3, 3]
