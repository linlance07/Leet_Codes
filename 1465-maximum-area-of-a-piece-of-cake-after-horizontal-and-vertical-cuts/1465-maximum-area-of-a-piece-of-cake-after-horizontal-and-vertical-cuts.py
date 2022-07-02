class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        H = [horizontalCuts[0]]
        V = [verticalCuts[0]]
        for i in range(1,len(horizontalCuts)):
            H.append(horizontalCuts[i]-horizontalCuts[i-1])
        for j in range(1,len(verticalCuts)):
            V.append(verticalCuts[j]-verticalCuts[j-1])
        H.append(h-horizontalCuts[-1])
        V.append(w-verticalCuts[-1])
        return (max(H)*max(V))%(10**9+7)
        