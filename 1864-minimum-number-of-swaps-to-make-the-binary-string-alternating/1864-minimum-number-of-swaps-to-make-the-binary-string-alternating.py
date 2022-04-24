class Solution:
    def minSwaps(self, s: str) -> int:
        one = s.count('1')
        zero = s.count('0')
        if one==zero or one+1==zero or zero+1==one:
            #1
            p1 = p2 = 0
            for i in range(len(s)):
                if i%2==0:
                    if s[i]=='0':
                        p1 += 1
                else:
                    if s[i]=='1':
                        p1 += 1
            #2
            for i in range(len(s)):
                if i%2==0:
                    if s[i]=='1':
                        p2 += 1
                else:
                    if s[i]=='0':
                        p2 += 1
            if p1%2==0 and p2%2==0:
                return min(p1//2,p2//2)
            if p1%2==0:
                return p1//2
            if p2%2==0:
                return p2//2                   
            
        return -1