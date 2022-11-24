import bisect

nums = [1, 2, 2, 2, 4, 7, 9]

print(bisect.bisect(nums, 3))
print(bisect.bisect_right(nums, 2))
print(bisect.bisect_left(nums, 2))

print(bisect.bisect(nums, 12))
