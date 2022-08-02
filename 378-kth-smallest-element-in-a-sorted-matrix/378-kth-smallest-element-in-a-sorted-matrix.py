class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in matrix:
            for j in i:
                heappush(arr,j)
        while k:
            a = heappop(arr)
            k -= 1
        return a
            