class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        toReturn = 0
        
        nums = Counter(arr[:1])
        for j in range(1, n - 1):
            for k in range(j + 1, n):
                toReturn = (toReturn + nums[target - arr[k] - arr[j]]) % 1000000007  
            nums[arr[j]] += 1

        return toReturn