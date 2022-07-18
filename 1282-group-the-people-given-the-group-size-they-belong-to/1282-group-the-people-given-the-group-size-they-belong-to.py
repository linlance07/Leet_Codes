class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        D = defaultdict(list)
        for j,i in enumerate(groupSizes):
            D[i].append(j)
        ans = []
        for i in D:
            if len(D[i])==i:
                ans.append(D[i])
            else:
                for j in range(0,len(D[i]),i):
                    ans.append(D[i][j:j+i])
        return ans
            
        