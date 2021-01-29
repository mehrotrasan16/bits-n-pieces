#Problem Moving Average from Data Stream
#https://nifannn.github.io/2018/10/01/Algorithm-Notes-Leetcode-346-Moving-Average-from-Data-Stream/
class MAFinder:

    def __init__(self,size):
        """
        initialize your data structure here.
        """
        mylist = []
        mysize = size
        

    def addNum(self, num: int) -> None:
        
        if len(mylist) < size:
            self.mylist.append(num)
        else:
            self.mylist.pop(0)
            self.mylist.append(num)
            
            
    def findMA(self) -> float:
        return sum(self.mylist)/self.mysize

# Your MedianFinder object will be instantiated and called as such:
obj = MAFinder()
obj.addNum(num)
param_2 = obj.findMA()
