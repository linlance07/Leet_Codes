class Solution:
    def isHappy(self, n: int) -> bool:
        a=0
        ans = list()
        try:
            while n!=1:
                for i in range(len(str(n))):
                    a = a+int(str(n)[i])**2
                #print(a)
                if a not in ans:
                    ans.append(a)
                else:
                    return False
                n=a
                a=0  
        except:
            return False
        return True