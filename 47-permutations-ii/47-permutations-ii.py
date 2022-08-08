class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        vis = set()
        def perm(arr,path):
            if len(arr)==0 and tuple(path) not in vis:
                ans.append(path)
                vis.add(tuple(path))
            for i in range(len(arr)):
                perm(arr[:i]+arr[i+1:],path+[arr[i]])    
        perm(nums,[])
        return ans