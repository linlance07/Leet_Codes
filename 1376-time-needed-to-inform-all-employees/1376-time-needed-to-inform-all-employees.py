class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for i in range(len(manager)):
            if manager[i]!=-1:
                tree[manager[i]].append(i)
        Q = [(informTime[headID],headID)]
        time = -float('inf')
        while Q:
            a,b = Q.pop(0)
            time = max(time,a)
            for _ in tree[b]:
                Q.append((informTime[_]+a,_))
        return time
                