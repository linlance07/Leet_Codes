#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        ans= ""
        fail = False
        for i in range(100):
            c = 0
            for j in arr:
                if i>=len(j):
                    fail = True
                    break
                if j[i]==arr[0][i]:
                    c += 1
            if fail:
                break
            if c==n:
                ans += arr[0][i]
            else:break
        if ans:
            return ans
        return -1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends