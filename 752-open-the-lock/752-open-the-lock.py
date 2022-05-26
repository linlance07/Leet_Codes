class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        visit = set("0000")
        Q = [("0000",0)]
        while Q:
            s,c = Q.pop(0)
            if s==target:
                return c
            if s in dead:
                continue
            for i in range(4):
                num = int(s[i])
                for j in [-1,1]:
                    n = (num + j) % 10
                    new = s[:i] + str(n) + s[i+1:]
                    if new not in visit:
                        visit.add(new)
                        Q.append((new,c+1))
        return -1
                    
                    
                
            