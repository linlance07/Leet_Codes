class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = {}
        ans = []
        for i in strs:
            I = "".join(sorted(i))
            if I not in D:
                D[I] = []
            D[I].append(i)
        for j in D:
            ans.append(D[j])
        return ans