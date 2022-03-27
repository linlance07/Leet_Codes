class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        D = Counter(nums)
        A = [(-j,i) for i,j in D.items()]
        heapify(ans)
        for l in A:
            heappush(ans,l)
        return [(heappop(ans)[1]) for _ in range(k)]
            
        