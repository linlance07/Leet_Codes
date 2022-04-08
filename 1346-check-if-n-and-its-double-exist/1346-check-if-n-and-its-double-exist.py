class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        D = {}
        for i in arr:
            if i*2 in D or i/2 in D:
                return True
            D[i] = 1
        return False