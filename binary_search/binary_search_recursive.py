def binary_search_recursive(arr, item, left=None, right=None):
    if left is None:
        left = 0

    if right is None:
        right = len(arr) - 1

    # Base case
    if left > right:
        return None

    mid = left + (right - left) // 2
    #print(mid)

    guess = arr[mid]

    if guess == item:
        return mid

    elif item > guess:
        return binary_search_recursive(arr, item, mid + 1, right)

    else:
        return binary_search_recursive(arr, item, left, mid - 1)

list = [4, 5, 6, 7, 8, 3, 2, 9]
sort_list = sorted(list)
print(sort_list)
print(binary_search_recursive(sort_list, 7))
print(binary_search_recursive(sort_list, -1))
