class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                A = s[:i] + s[i+1:]
                B = s[:j] + s[j+1:]
                if A==A[::-1] or B==B[::-1]:
                    return True
                else:
                    return False        
            i+=1
            j-=1
        return True
            