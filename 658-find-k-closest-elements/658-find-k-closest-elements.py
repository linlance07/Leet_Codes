class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            heappush(heap,(abs(x-i),i))
        ans = []
        while k:
            k -= 1
            ans.append(heappop(heap)[1])
        return sorted(ans)