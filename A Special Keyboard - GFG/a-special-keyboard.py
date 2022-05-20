#User function Template for python3

class Solution:
    def findTime(self, S1, S2):
        D = {}
        for i in range(len(S1)):
            D[S1[i]] = i
        ans = 0
        prev = 0
        for j in S2:
            curr = abs(D[j] - prev)
            ans += curr
            prev = D[j]
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1=input()
        S2=input()
        
        ob = Solution()
        print(ob.findTime(S1,S2))
# } Driver Code Ends