#User function Template for python3

class Solution:
    def permutation (self, S):
        s = [""]*(2*len(S)-1)
        i = 0
        j = 0
        while i<len(S):
            s[j] = S[i]
            i += 1
            j += 2
        ans = []
        n = (2**(len(S)-1))-1
        l = [x for x in range(1,len(s),2)]
        for k in range(n,-1,-1):
            a = bin(k)[2:]
            b = '0'*(len(l)-len(a)) + a
            ind = 0
            ss = s.copy()
            for m in range(len(l)):
                if b[m]=='1':
                    ss[l[ind]] = " "
                ind += 1
            ans.append("".join(ss))
        return ans
                    


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends