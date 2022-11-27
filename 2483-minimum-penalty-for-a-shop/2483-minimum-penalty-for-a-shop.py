class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pre = [0]
        suf = [0]
        for i in customers:
            if i=='Y':
                pre.append(pre[-1])
            else:
                pre.append(pre[-1]+1)
        for i in customers[::-1]:
            if i=='Y':
                suf.append(suf[-1]+1)
            else:
                suf.append(suf[-1])
        suf = suf[::-1]
        pen = float('inf')

        for i in range(len(pre)):
            if suf[i]+pre[i]<pen:
                pen = suf[i] + pre[i]
                ans = i
        return ans
        