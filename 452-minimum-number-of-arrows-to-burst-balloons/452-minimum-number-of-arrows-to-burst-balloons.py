class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        prev = None
        ans = 1
        points.sort()
        print(points)
        for i in range(len(points)):
            if i==0:
                prev = points[i]
            else:
                st = points[i][0]
                en = points[i][1]
                if st>=prev[0] and st<=prev[1]:
                    prev[1] = min(en,prev[1])
                    continue
                ans += 1
                prev = points[i]
        return ans