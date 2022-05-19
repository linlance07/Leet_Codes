#Back-end complete function Template for Python 3

class Solution:
    def transform(self, A, B): 
        i = len(A) - 1
        j = len(B) - 1
        H1 = [0]*52
        H2 = [0]*52
        if len(A)!=len(B):
            return -1
        for k in range(len(A)):
            if ord(A[k])<97:
                H1[ord(A[k]) - 97 + 26] += 1
            else:
                H1[ord(A[k]) - 97] += 1
            if ord(B[k])<97:
                H2[ord(B[k]) - 97 + 26] += 1
            else:
                H2[ord(B[k]) - 97] += 1
        if H1!=H2:
            return -1
        ans = 0
        while i>=0 and j>=0:
            if A[i]==B[j]:
                i -= 1
                j -= 1
            else:
                i -= 1
                ans += 1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        ob = Solution()
        print(ob.transform(A,B))
# } Driver Code Ends