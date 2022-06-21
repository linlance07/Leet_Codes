class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        C = Counter(arr)
        heap = []
        for i,j in C.items():
            heappush(heap,-j)
        ans = 0
        tot = len(arr)
        lim = len(arr)//2
        while heap:
            if tot<=lim:
                break
            tot -= abs(heappop(heap))
            ans += 1
        return ans
            