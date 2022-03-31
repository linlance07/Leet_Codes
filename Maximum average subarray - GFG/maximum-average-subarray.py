#User function Template for python3

class Solution:
    def findMaxAverage(self, arr, n, k):
        st = 0
        avg = 0.0
        s = 0
        ans = []
        for i in range(k):
            s += arr[i]
        avg = s/k
        res = 0
        for j in range(k,n):
            s -= arr[st]
            st += 1
            s += arr[j]
            if avg<s/k:
                res = st
                avg = s/k
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxAverage(arr, n, k)
        for i in range(ans, ans+k):
            print(arr[i], end=" ")
        print()
        tc -= 1
# } Driver Code Ends