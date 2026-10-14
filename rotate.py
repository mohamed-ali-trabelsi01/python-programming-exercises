def rotate_list(liste, positionen):

    n = len(liste)
    if n == 0:
        return liste


    positionen = positionen % n
    if positionen == 0:
        return liste


    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(liste, 0, n - 1)

    reverse(liste, 0, positionen - 1)

    reverse(liste, positionen, n - 1)

    return liste



liste = [1,2,3,4,5,6,7]
print(rotate_list(liste, 3))   # -> [5,6,7,1,2,3,4]

liste = [1,2,3]
print(rotate_list(liste, 0))   # -> [1,2,3]

liste = [1,2,3,4]
print(rotate_list(liste, 4))   # -> [1,2,3,4]

liste = [1,2,3]
print(rotate_list(liste, 4))   # -> [3,1,2]

liste = [-1,-100,3,99]
print(rotate_list(liste, 3))   # -> [-100,3,99,-1]
