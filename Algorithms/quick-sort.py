def qs(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return qs(left) + middle + qs(right)

nums = [3, 6, 8, 10, 1, 2, 1]
sorted_nums = qs(nums)
print(f"Sorted array: {sorted_nums}")  # Output: Sorted array: [1, 1, 2, 3, 6, 8, 10]

# ONE LINER FOR QUICK SORT
qs = lambda nums: nums if len(nums) <= 1 else qs([x for x in nums if x < nums[len(nums) // 2]]) + [nums[len(nums) // 2]] * nums.count(nums[len(nums) // 2]) + qs([x for x in nums if x > nums[len(nums) // 2]])
