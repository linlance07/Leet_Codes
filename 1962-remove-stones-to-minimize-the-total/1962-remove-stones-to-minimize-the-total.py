class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        arr = []
        heapify(arr)
        ans = 0
        for i in piles:
            ans += i
            heappush(arr,-i)
        while k:
            k -= 1
            a = -heappop(arr)
            ans = ans - a + ceil(a/2)
            heappush(arr,-ceil(a/2))
        return ans