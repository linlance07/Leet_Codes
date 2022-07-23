class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        Q = [(0,0)]
        jump = 0
        F = set(forbidden)
        while Q:
            n = len(Q)
            #print(Q)
            for _ in range(n):
                q,act = Q.pop(0)
                if q==x:
                    return jump
                if q in F or (q,act) in F:
                    continue
                F.add((q,act))
                r = q + a
                l = q - b
                if r<100000:
                    Q.append((r,0))
                if l>=0 and act==0:
                    Q.append((l,1))
            
            jump += 1
        return -1
                