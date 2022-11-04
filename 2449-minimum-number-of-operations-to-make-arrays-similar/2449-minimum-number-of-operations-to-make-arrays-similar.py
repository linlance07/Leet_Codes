class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        odd = []
        odd_t = []
        even = []
        even_t = []
        for i in nums:
            if i%2:
                odd += [i]
            else: 
                even += [i]
        for i in target:
            if i%2:
                odd_t += [i]
            else:
                even_t += [i]
        odd.sort()
        odd_t.sort()
        even.sort()
        even_t.sort()
        ans = 0
        for i in range(len(odd)):
            d =odd[i]-odd_t[i]
            ans += d if d>=0 else 0
        for i in range(len(even)):
            d = even[i]-even_t[i]
            ans +=d if d>=0 else 0
        return ans//2
            
        