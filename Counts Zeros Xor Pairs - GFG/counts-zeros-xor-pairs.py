#User function Template for python3

from collections import defaultdict
def calculate (arr, n) : 
    D = defaultdict(lambda:0)
    ans = 0
    for i in range(n):
        ans += D[arr[i]]
        D[arr[i]] += 1
    return ans
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = calculate(arr, n)
    print(res)


# } Driver Code Ends