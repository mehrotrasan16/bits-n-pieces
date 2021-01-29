#ref from trajansmith's gist here: https://gist.github.com/trajamsmith/15bbffa937eb081e44823f86c6bd3603

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
               
        s = deque()
        
        
        while k - 26 > n - 1:
            s.append('z')
            k -= 26
            n -= 1
            
        mid = 0
        while n > 1:
            s.appendleft('a')
            k -= 1
            n -= 1
            mid += 1
        
        s.insert(mid, chr((k - 1) + ord('a')))
        
        return "".join(s)
