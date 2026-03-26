# write a recursive function to count the number of items in an array

def count(arr):
    if not arr:
        return 0

    return 1 + count(arr[1:])

array = [2, 4, 5, 7]
print("Sum: ", count(array))
