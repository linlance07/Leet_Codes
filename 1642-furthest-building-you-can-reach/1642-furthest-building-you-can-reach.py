class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        for i in range(len(heights)-1):
            h = heights[i+1] - heights[i]
            if h>0:
                heappush(arr,h)
            if len(arr)>ladders:
                bricks -= heappop(arr)
            if bricks<0:
                return i
        return len(heights) - 1