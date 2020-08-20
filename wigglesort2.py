nums = [1, 5, 1, 1, 6, 4]
dec = nums.copy()
dec.sort() #1,1,1,4,5,6
decindex = len(nums)-1
#odd position
for i in range(1,len(nums),2): nums[i] = dec[decindex]; decindex -=1

#even positionj
for i in range(0, len(nums),2): nums[i] = dec[decindex]; decindex -=1

print(nums)