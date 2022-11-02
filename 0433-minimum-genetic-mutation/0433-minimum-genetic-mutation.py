class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1
        bank = set(bank)
        bank.add(start)
        if end not in bank:
            return -1
        Q = [(start,0)]
        visit = set()
        while Q:
            s,c = Q.pop(0)
            if s==end:
                print(s)
                return c
            if s not in bank:
                continue
            for i in range(8):
                curr = s[i]
                for j in "ACGT":
                    if curr!=j:
                        new = s[:i] + j + s[i+1:]
                        #print(new)
                        if new not in visit:
                            visit.add(new)
                            Q.append((new,c+1))                 
        return -1