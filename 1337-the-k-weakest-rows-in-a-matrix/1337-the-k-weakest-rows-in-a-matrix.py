class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        heapify(ans)
        for i in range(len(mat)):
            flag = 1
            for j in range(len(mat[0])-1,-1,-1):
                if mat[i][j]:
                    heappush(ans,(j+1,i))
                    flag = 0
                    break
            if flag:
                heappush(ans,(0,i))
        res = []
        for x in range(k):
            res.append(heappop(ans)[1])
        return res