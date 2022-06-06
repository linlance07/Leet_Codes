class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = (0,"")
        for i in dictionary:
            x = y = 0
            while x<len(i) and y<len(s):
                if i[x]==s[y]:
                    x += 1
                    y += 1
                else:
                    y += 1
            if x==len(i):
                if len(i)>ans[0]:
                    ans = (len(i),i)
                elif len(i)==ans[0]:
                    if i<=ans[1]:
                        ans = (len(i),i)
        return ans[1]