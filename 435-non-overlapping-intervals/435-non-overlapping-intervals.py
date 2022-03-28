class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        I = intervals
        I.sort()
        prev = (0,0)
        ans = 0
        for i in range(len(I)):
            if i==0:
                prev = I[i]
            else:
                st = I[i][0]
                en = I[i][1]
                if st<prev[1]:
                    if prev[1]>en:
                        prev = I[i]
                    ans += 1
                else:
                    prev = I[i]
        return ans
        