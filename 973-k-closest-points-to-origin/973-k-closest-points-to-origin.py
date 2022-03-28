class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for i in points:
            a = i[0]
            b = i[1]
            c = (a**2) + (b**2)
            arr.append((c,a,b))
        arr.sort()
        ans = []
        for n in range(k):
            ans.append([arr[n][1],arr[n][2]])
        return ans