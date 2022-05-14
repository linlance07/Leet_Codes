class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(dist)):
            a = dist[i]
            b = speed[i]
            c = int(ceil(a/b))
            arr.append((c,a,b)) #time,distance,speed
        arr.sort()
        ans = 0
        time = 0
        for j in range(len(arr)):
            if arr[j][0]>time:
                ans += 1
                time += 1
            else:
                break
        return ans