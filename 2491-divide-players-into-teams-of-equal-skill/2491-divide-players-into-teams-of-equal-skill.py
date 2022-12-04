class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        s = set()
        for i in range(len(skill)//2):
            ans += skill[i] * skill[len(skill)-i-1]
            s.add(skill[i]+skill[len(skill)-i-1])
        return ans if len(s)==1 else -1
            