class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global ans
        ans = []
        def combi(s,path,ind):
            if s>target:
                return
            if s==target:
                ans.append(path)
                return
            for _ in range(ind,len(candidates)):
                combi(s+candidates[_],path+[candidates[_]],_)
        combi(0,[],0)  #sum,path,index
        return ans