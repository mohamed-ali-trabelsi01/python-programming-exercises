def binary_recursive(lst, key, low=0, high=None):

    if high is None:
        high = len(lst) - 1


    if low > high:
        return -1

    mid = (low + high) // 2


    if lst[mid] == key:
        return mid


    elif key < lst[mid]:
        return binary_recursive(lst, key, low, mid - 1)


    else:
        return binary_recursive(lst, key, mid + 1, high)


print(binary_recursive([6, 7, 8, 9, 10], 8))        # Erwartet: 2
print(binary_recursive([11, 13, 15, 17, 18], 17))   # Erwartet: 3
print(binary_recursive([3, 4, 5, 6, 7], 1))         # Erwartet: -1
print(binary_recursive([], 13))                     # Erwartet: -1
    