class Solution:
    def makeGood(self, s: str) -> str:
        cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sma = "abcdefghijklmnopqrstuvwxyz"
        ans = []
        for i in s:
            if not ans:
                ans.append(i)
            else:
                if ans[-1].isupper() and i.islower():
                    a = cap.index(ans[-1])
                    b = sma.index(i)
                    if a==b:
                        ans.pop()
                        continue
                elif ans[-1].islower() and i.isupper():
                    a = sma.index(ans[-1])
                    b = cap.index(i)
                    if a==b:
                        ans.pop()
                        continue
                ans.append(i)
        return "".join(ans)