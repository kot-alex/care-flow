import math


def linear_search(lst, value, key=None):
    for item in lst:
        if key is not None:
            if key(item) == value:
                return item
        else:
            if item == value:
                return item
    return None


def binary_search(arr, target, low=0, high=None, key=None):
    if high is None:
        high = len(arr) - 1  # Default to last index if no high

    while low <= high:
        mid = (low + high) // 2
        mid_value = key(arr[mid]) if key else arr[mid]

        if mid_value == target:
            return arr[mid]
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # The block size is the square root of n
    prev = 0

    while arr[min(step, n) - 1].patient_id < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None  # Element is not present

    # Linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i].patient_id == target:
            return arr[i]  # Return the patient object
    return None


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while (
        low <= high and target >= arr[low].patient_id and target <= arr[high].patient_id
    ):
        # Estimate the position using interpolation formula
        pos = low + int(
            (
                (float(high - low) / (arr[high].patient_id - arr[low].patient_id))
                * (target - arr[low].patient_id)
            )
        )

        if arr[pos].patient_id == target:
            return arr[pos]
        elif arr[pos].patient_id < target:
            low = pos + 1
        else:
            high = pos - 1
    return None


def exponential_search(arr, target):
    if arr[0].patient_id == target:
        return arr[0]  # Return the patient object

    # Find range for binary search by doubling the index
    n = len(arr)
    i = 1
    while i < n and arr[i].patient_id <= target:
        i *= 2

    # Perform binary search in the range [i/2, min(i, n-1)]
    return binary_search(arr, target, i // 2, min(i, n - 1))
