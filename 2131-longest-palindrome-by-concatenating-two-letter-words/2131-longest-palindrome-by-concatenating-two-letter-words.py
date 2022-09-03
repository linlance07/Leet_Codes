class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        D = defaultdict(int)
        doub = defaultdict(int)
        #print(Counter(words))
        ans = 0
        for i in words:
            if i[::-1]==i:
                doub[i] += 1
            elif i[::-1] in D:
                ans += 4
                D[i[::-1]] -= 1
                if D[i[::-1]]==0:
                    del D[i[::-1]]
            else:
                D[i] += 1
            #print(i,D,ans)
        one = 0
        if doub:
            for i in doub:
                if doub[i]%2==0:
                    ans += doub[i] * 2
                else:
                    ans += (doub[i] - 1) * 2
                    one = 1                
        if one:
            ans += 2
        return ans