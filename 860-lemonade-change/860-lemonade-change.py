class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ihave = 0
        doll = {5:0,10:0,20:0}
        for i in bills:
            if i==5:
                doll[5] += 1
            elif i==10:
                if doll[5]:
                    doll[5] -= 1
                    doll[10] += 1
                else:
                    return False
            else:
                if doll[5] and doll[10]:
                    doll[10] -= 1
                    doll[5] -= 1
                elif doll[5]>=3:
                    doll[5]-=3
                else:
                    return False
                doll[20] += 1
        return True 