class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        D = Counter(words)
        ans = []
        A = [(-j,i) for i,j in D.items()]
        heapify(ans)
        for l in A:
            heappush(ans,l)
        res = []
        while k:
            k-=1
            res.append(heappop(ans)[1])
        return res