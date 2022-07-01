class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr = sorted(boxTypes,key = lambda x: -x[1])
        ans = 0
        for i,j in arr:
            ans += min(truckSize,i)*j
            truckSize -= min(truckSize,i)
            if not truckSize:
                break
        return ans