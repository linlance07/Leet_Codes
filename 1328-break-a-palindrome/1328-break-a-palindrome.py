class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        for i in range(len(palindrome)):
            if palindrome[i]!='a':
                if i==len(palindrome)//2 and len(palindrome)%2:
                    continue
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[0:len(palindrome)-1] + 'b'