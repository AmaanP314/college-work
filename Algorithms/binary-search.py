def bs(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (r + l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = bs(nums, target)
print(f"Element found at index: {result}")  # Output: Element found at index: 4