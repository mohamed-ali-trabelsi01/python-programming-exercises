def linear_search(lst, key):
    # liste durchgehen
    for i in range(len(lst)):
        if lst[i] == key:
            return i

    return -1


# tests
print(linear_search([1, 2, 3], 2))
print(linear_search([5, 4, 3, 2, 1], 3))
print(linear_search([1, 2, 3], 10))
print(linear_search([], 10))
