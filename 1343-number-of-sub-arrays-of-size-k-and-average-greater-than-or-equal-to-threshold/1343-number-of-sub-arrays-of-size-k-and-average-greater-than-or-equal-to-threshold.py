class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = 0
        ans = 0
        for i in range(len(arr)):
            if i<k:
                s += arr[i]
                if i+1==k:
                    if s/k>=threshold:
                        ans += 1                
            else:
                s += arr[i]
                s -= arr[i-k]
                if s/k>=threshold:
                    ans += 1
        return ans