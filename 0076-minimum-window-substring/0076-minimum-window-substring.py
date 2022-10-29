class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = Counter(t)
        l = 0
        r = 0
        ans = None
        D = Counter()
        while r<len(s):
            flag = 0
            D[s[r]] += 1
            while True:
                for i in T:
                    if T[i]>D[i]:
                        flag = 1
                        break
                if flag:
                    break
                if ans==None:
                    ans = (l,r)
                else:
                    if (r-l)<=(ans[1]-ans[0]):
                        ans = (l,r)
                # print(ans,l,r)
                D[s[l]] -= 1
                l += 1
            r += 1
        return s[ans[0]:ans[1]+1] if ans!=None else ""
                    
            