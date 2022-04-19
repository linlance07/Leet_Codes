class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        alpha = [0]*26
        for i in p:
            alpha[ord(i)-97] += 1
        st = 0
        new_alpha = [0]*26
        for j in range(len(p)):
            a = ord(s[j])-97
            new_alpha[a] += 1
        ans = []
        if alpha==new_alpha:
            ans.append(st)
        for k in range(len(p),len(s)):
            b = ord(s[st])-97
            st+=1
            c = ord(s[k])-97
            new_alpha[b]-=1
            new_alpha[c]+=1
            if alpha==new_alpha:
                ans.append(st)
        return ans
                