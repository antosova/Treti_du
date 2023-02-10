array = [2, 8, 4, 12, 6, 1, 10]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j != 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

print('unsorted: ' + str(array))

sorted = insertion_sort(array)

print('sorted: ' + str(sorted))