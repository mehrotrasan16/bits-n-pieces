from math import prod
nums = [10,5,2,6] #[1,1,1]#[10,5,2,6]
k = 100

#Ans [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
#Corner Case [1,1,1], k = 2 -> breaks the below code becuase i''m removing duplicates

sarr= []

for i in range(len(nums)):
    #print(nums[i])
    for window in range(len(nums)+1):
        print(window)
        if(i + window <= len(nums)):    #So that the i + window doesn't cross the length of the array
            temp = nums[i:i+window]
            print(i,i+window,temp)

            try:
                if(prod(temp) < k and temp != []):
                    sarr.append(temp)
                    print(sarr)
            except:
                pass

# sarr.sort()
# dedup = [sarr[i] for i in range(len(sarr)) if i == 0 or sarr[i] != sarr[i-1] ]
# print(dedup,len(dedup))

print(sarr)

# The below works, but its slow. Calculating the sub arrays takes too much time
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    sarr= []

    for i in range(len(nums)):
        for window in range(len(nums)+1):
            if(i + window <= len(nums)):
                temp = nums[i:i+window]
                if(prod(temp) < k and temp != []):
                    sarr.append(temp)
    return len(sarr)