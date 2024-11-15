def bubble_sort(arr, key=None):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key:
                if key(arr[j]) > key(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr, key=None):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and (key(arr[j]) > key(key_item) if key else arr[j] > key_item):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


def merge_sort(arr, key=None):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if key:
                if key(left_half[i]) < key(right_half[j]):
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            else:
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
