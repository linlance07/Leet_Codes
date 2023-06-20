from typing import List


class Solution:
    def maxEqualSum(self, N1:int,N2:int,N3:int, S1 : List[int], S2 : List[int], S3 : List[int]) -> int:
        asum = sum(S1)
        a = {asum}
        for i in S1:
            asum -= i
            a.add(asum)
        bsum = sum(S2)
        b = {bsum}
        for i in S2:
            bsum -= i
            b.add(bsum)
        csum = sum(S3)
        c = {csum}
        for i in S3:
            csum -= i
            c.add(csum)
        d = sorted(a.intersection(b,c),reverse=True)
        return d[0] if d else 0
        
            
        



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
        
        a=IntArray().Input(3)
        
        
        S1=IntArray().Input(a[0])
        
        
        S2=IntArray().Input(a[1])
        
        
        S3=IntArray().Input(a[2])
        
        obj = Solution()
        res = obj.maxEqualSum(a[0],a[1],a[2], S1, S2, S3)
        
        print(res)
        

# } Driver Code Ends