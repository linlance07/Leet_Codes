class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        heapify(arr)
        for i in stones:
            heappush(arr,-i)
        while len(arr)>1:
            a = abs(heappop(arr))
            b = abs(heappop(arr))
            if a!=b:
                heappush(arr,-abs(a-b))
        if arr:
            return -arr[0]
        return 0
            