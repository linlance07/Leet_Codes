class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        D = Counter(nums)
        ans = 0
        for i in range(len(target)):
            a = target[:i+1]
            b = target[i+1:]
            print(a,b)
            if a in D and b in D:
                if a==b:
                    ans += (D[b] - 1) * D[a]
                else:
                    ans += D[a] * D[b]
        return ans
            