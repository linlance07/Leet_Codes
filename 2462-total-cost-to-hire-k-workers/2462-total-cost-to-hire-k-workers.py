class Solution:
    def totalCost(self, costs: List[int], k: int, c: int) -> int:
        left = []
        right = []
        ans = 0
        if c+c>=len(costs) or k==len(costs):
            arr = sorted(costs)
            return sum(arr[:k])
        else:
            for i in range(c):
                heappush(left,costs[i])
                heappush(right,costs[len(costs)-i-1])
            l = c
            r = len(costs) - c - 1
            while k:
                a = left[0] if left else float('inf')
                b = right[0] if right else float('inf')
                if a<b:
                    ans += a
                    heappop(left)
                    if l<=r:
                        heappush(left,costs[l])
                        l += 1
                elif a>b:
                    ans += b
                    heappop(right)
                    if l<=r:
                        heappush(right,costs[r])
                        r -= 1
                else:
                    ans += a
                    heappop(left)
                    if l<=r:
                        heappush(left,costs[l])
                        l += 1
                k -= 1
            return ans
        