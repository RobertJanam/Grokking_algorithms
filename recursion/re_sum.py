# write a recursive function that sums up items(integers) in an array

def summation(arr):
    if not arr:
        return 0

    return arr[0] + summation(arr[1:])

array = [2, 4, 5, 7]
print("Sum: ", summation(array))
