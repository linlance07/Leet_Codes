class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        for i in range(len(s)):
            if i==len(s)-1:
                a = s[i]
                b = s[0]
            else:
                a = s[i]
                b = s[i+1]
            if a[-1]!=b[0]:
                return False
        return True