class Solution:
    def minJumps(self, arr: List[int]) -> int:
        D = defaultdict(list)
        for j in range(len(arr)-1,-1,-1):
            D[arr[j]] += [j]
        Q = []
        heapify(Q)
        heappush(Q,(0,0))
        visit = [True]*len(arr)
        while Q:
            n = len(Q)
            for __ in range(n):
                jmp , ind = heappop(Q)
                if ind==len(arr)-1:
                    return jmp
                if not visit[ind]:
                    continue
                visit[ind] = False
                if ind!=0:
                    l = ind - 1
                    heappush(Q,(jmp+1,l))
                if ind!=len(arr)-1:
                    r = ind + 1
                    heappush(Q,(jmp+1,r))
                for _ in D[arr[ind]]:
                    heappush(Q,(jmp+1,_))
                D[arr[ind]].clear()
                
            
            
            