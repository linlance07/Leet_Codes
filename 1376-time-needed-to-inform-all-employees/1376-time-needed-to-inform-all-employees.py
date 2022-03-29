class Solution(object):
    def numOfMinutes(self, n, h, m, t):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        d=defaultdict(list)
        if n==1:
            return 0
        for i in range(n):
            d[m[i]].append(i)
        #print(d)
        r=d[-1][0]
        q=[(t[r],r)]
        m=-float("inf")
        while q:
            x,y=q.pop(0)
            m=max(m,x)
            for i in d[y]:
                q.append((x+t[i],i))
        return m
                
            
        