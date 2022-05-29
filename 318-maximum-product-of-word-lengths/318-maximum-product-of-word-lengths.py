class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit = [0]*len(words)
        for i in range(len(words)):
            for j in words[i]:
                bit[i] |= 1<<(ord(j)-97)
        ans = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if bit[i]&bit[j]==0:
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans