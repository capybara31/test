def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_item = array[mid]
        if target == mid_item:
            return mid
        elif target > mid_item:
            low = mid + 1
        else:
            high = mid - 1
    return None
