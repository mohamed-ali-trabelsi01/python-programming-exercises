def bubble_sort(lst):
    """
    Sortiert die Liste lst mittels Bubble-Sort in aufsteigender Reihenfolge.
    """
    n = len(lst)


    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst





print(bubble_sort([3, 2, 4, 1]))       # -> [1, 2, 3, 4]
print(bubble_sort([1, 2, 3, 4, 5, 6])) # -> [1, 2, 3, 4, 5, 6]
print(bubble_sort([3, 1, 3, 2, 3, 4])) # -> [1, 2, 3, 3, 3, 4]
