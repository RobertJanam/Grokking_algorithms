def quicksort(arr):
    # base case
    if len(arr) < 2:
        return arr

    else:
        # pivot
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

array = [6, 3, 7, 2, 5, 1, 4]

print(quicksort(array))
