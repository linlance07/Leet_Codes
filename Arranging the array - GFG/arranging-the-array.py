
from typing import List


class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        neg = []
        pos = []
        for i in arr:
            if i<0:
                neg += [i]
            else:
                pos += [i]
        arr[:] = neg + pos
        return arr
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(2)
        
        obj = Solution()
        obj.Rearrange(n, arr)
        
        print(*arr, end=' ')
        print()

# } Driver Code Ends