import bisect


def bisect_function(nums, value, low, high):
    if high < low:
        return -1
    half_index = low + (high - low) // 2
    if nums[half_index] == value:
        return half_index
    elif nums[half_index] < value:
        return bisect_function(nums, value, half_index + 1, high)
    else:
        return bisect_function(nums, value, low, half_index - 1)


print(bisect_function([1, 2, 3], 3, 0, 2))
