def searchInsert(lst, key):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == key:
            return mid

        if lst[mid] < key:
            left = mid + 1
        else:
            right = mid - 1


    return left


# tests
print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
print(searchInsert([1, 3, 5, 6], 0))  
