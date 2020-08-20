#Simple,easy life insert, sort and calculate
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.list = []
        
#     def addNum(self, num: int) -> None:
#         self.list.append(num)

#     def findMedian(self) -> float:
#         self.list.sort()
#         length = len(self.list)
#         return self.list[length//2] if length%2 == 1 else ((self.list[length//2-1] + self.list[length//2]) * 0.5)

#Insertion sort preserves order while inserting element, making median calls quicker.
# Improvement time: almost half, Imp space: almost the same. 
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.list = []
        

#     def addNum(self, num: int) -> None:
#         if(len(self.list) == 0):
#             self.list.append(num)
#         else:
#             #insertion sort in a python list
#             self.list.sort()
#             lo=0
#             hi=len(self.list)
#             while lo < hi:
#                 mid = (lo+hi)//2
#                 if num < self.list[mid]:
#                     hi = mid
#                 else:
#                     lo = mid+1
#             self.list.insert(lo, num)

#     def findMedian(self) -> float:
#         length = len(self.list)
#         return self.list[length//2] if length%2 == 1 else ((self.list[length//2-1] + self.list[length//2]) * 0.5)
#         #index = len/2 if len %2 == 1 else len/2 +1

##Two heaps Reference code:  https://leetcode.com/problems/find-median-from-data-stream/discuss/278272/Python-Two-Heaps
class MedianFinder(object):

    def __init__(self):
        self.med, self.odd, self.heaps = 0, 0, [[], []]

    def addNum(self, x):
        big, small = self.heaps
        if self.odd:
            heapq.heappush(big, max(x, self.med))
            heapq.heappush(small, -min(x, self.med))
            self.med = (big[0] - small[0]) / 2.0
        else:
            if x > self.med:
                self.med = heapq.heappushpop(big, x)
            else:
                self.med = -heapq.heappushpop(small, -x)
        self.odd ^= 1

    def findMedian(self):
        return self.med

#Two heaps ref code #2: 
class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

#my submission
from heapq import *
class MedianFinder:

    def __init__(self):
        self.heaps = [[],[]]
        
    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heappush(small, -heappushpop(large,num))
        if(len(large) < len(small)):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)