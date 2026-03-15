# finds the smallest element in the list and returns its index
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):
    newArr = []
    copiedArr = list(arr) # makes the var a list object and copies arr elements exceeding any mutations

    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest)) # removes the smallest element in the copiedArr and adds it to the newArr

    return newArr

array = [3, 2, 6, 8, 1, 5, 4]
print(selection_sort(array))
