def binary_search(arr, item):
    high = len(arr) - 1 #last index in the list
    low = 0 # first index in the list

    while low <= high:
        mid = (high + low) // 2 # returns a rounded off number
        guess = arr[mid] # gets the actual element
        if guess == item:
            return mid # returns index of the element

        if item > guess: # item is greater than the mid
            low = mid + 1 # discards every element lower than mid including mid

        else:
            high = mid - 1 # discards every element higher than mid including mid

    return None # item is not found in the list

list = [4, 5, 6, 7, 8, 3, 2, 9]
sort_list = sorted(list)
print(binary_search(sort_list, 7))
print(binary_search(sort_list, -1))
