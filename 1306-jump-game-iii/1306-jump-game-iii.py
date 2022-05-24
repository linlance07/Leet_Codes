class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        Q = [start]
        ans = False
        n = len(arr)
        visit = [True for __ in range(n)]
        while Q:
            N = len(Q)
            for _ in range(N):
                q = Q.pop(0)
                if arr[q]==0:
                    return True
                visit[q] = False
                l = q - arr[q]
                r = q + arr[q]
                if l>=0 and visit[l]:
                    if arr[l]==0:
                        return True
                    Q.append(l)
                if r<len(arr) and visit[r]:
                    if arr[r]==0:
                        return True
                    Q.append(r)
        return False