def binary_search(lst, key):
    low = 0
    high = len(lst) - 1


    while low <= high:
        mid = (low + high) // 2   # mitte berechnen


        if lst[mid] == key:
            return mid


        if lst[mid] < key:
            low = mid + 1
        else:

            high = mid - 1


    return -1


# ein paar tests
print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5], 5))
print(binary_search([1, 2, 3, 4, 5], 0))
print(binary_search([], 10))
