class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        D = Counter(nums)
        heapify(arr)
        for i,j in D.items():
            heappush(arr,(-j,i))
        ans = []
        for l in range(k):
            ans.append(heappop(arr)[1])
        return ans
            
        