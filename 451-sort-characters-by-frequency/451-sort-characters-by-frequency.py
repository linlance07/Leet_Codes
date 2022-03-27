class Solution:
    def frequencySort(self, s: str) -> str:
        D = Counter(s)
        ans = []
        heapify(ans)
        A = [(-j,i) for i,j in D.items()]
        for k in A:
            heappush(ans,k)
        string = ""
        while ans:
            a,b = heappop(ans)
            string += (b*(-a))
        return string