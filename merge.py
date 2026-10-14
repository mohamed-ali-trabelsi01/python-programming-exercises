def merge(lst1, lst2):
    """
    Führt zwei sortierte Listen lst1 und lst2 zu einer neuen,
    ebenfalls sortierten Liste zusammen.
    Die Original-Listen bleiben unverändert.
    """
    merged = []
    i = 0
    j = 0   

    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1


    while i < len(lst1):
        merged.append(lst1[i])
        i += 1

    while j < len(lst2):
        merged.append(lst2[j])
        j += 1

    return merged


print(merge([1, 3, 5], [2, 4, 6]))
# -> [1, 2, 3, 4, 5, 6]

print(merge([], [1, 2, 3]))
# -> [1, 2, 3]

print(merge([1, 2, 2], [2, 3]))
# -> [1, 2, 2, 2, 3]
