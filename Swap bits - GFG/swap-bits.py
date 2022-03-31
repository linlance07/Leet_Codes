#User function Template for python3

class Solution:
    def swapBits(self, X, P1, P2, N):
        b = bin(X)[2:]
        b = '0'*(32-len(b)) + b
        lis = []
        for i in b:
            lis.append(i)
        n = len(b)
        P1 = n-P1-1
        P2 = n-P2-1
        #print(P1,P2,lis)
        for j in range(N):
            lis[P1],lis[P2] = lis[P2],lis[P1]
            P1 -= 1
            P2 -= 1
        ans = "".join(lis)
        #print(ans)
        return int(ans,2)



#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))
        

# } Driver Code Ends