#User function Template for python3

class Solution:
    def minVal(self, a, b):
        B = bin(b)[2:]
        b_one = B.count('1')
        A = bin(a)[2:]
        ans = []
        for i in range(len(A)):
            if A[i]=='1':
                if b_one:
                    ans.append('1')
                    b_one -= 1
                else:
                    ans.append('0')
            else:
                ans.append('0')
        for j in range(len(A)-1,-1,-1):
            if ans[j]=='0':
                if b_one:
                    ans[j] = '1'
                    b_one -= 1
        if b_one:
            ans = (['1']*b_one) + ans
        x = "".join(ans)
        return int(x,2)
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = int(input())
        
        ob= Solution()
        print(ob.minVal(a,b))
# } Driver Code Ends