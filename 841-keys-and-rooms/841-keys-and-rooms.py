class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = [False for _ in range(n)]
        visit[0] = True
        Q = []
        for i in rooms[0]:
            Q.append(i)
        while Q:
            a = Q.pop(0)
            visit[a] = True
            for j in rooms[a]:
                if visit[j]==False:
                    Q.append(j)
        if all(visit):
            return True
        return False
            