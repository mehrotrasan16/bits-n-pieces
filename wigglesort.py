# Problem Statement: Wiggle sort
# Wiggle Sort
# Questions

# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is `[1, 6, 2, 5, 3, 4].

#Two solutions: 
# # 1. sort and swap
nums = [3, 5, 2, 1, 6, 4]

nums.sort() #1,2,3,4,5,6
temp = 0
#dupcheck = 0
for i in range(2, len(nums),2):
    temp = nums[i-1]
    nums[i-1] = nums[i]
    nums[i] = temp
    print(nums)

print(f"Final:{nums}")


# 2. one pass swap O[n], O[1]
nums = [3, 5, 2, 1, 6, 4]
for i in range(len(nums)):
    if((i%2 == 1 and nums[i] < nums[i-1]) or (i % 2 == 0 and nums[i] > nums[i-1])):
        temp = nums[i-1]
        nums[i-1] = nums[i]
        nums[i] = temp
        print(nums)

print(f"Final:{nums}")