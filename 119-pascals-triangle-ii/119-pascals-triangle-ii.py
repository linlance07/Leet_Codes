class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(rowIndex+1):
            if rowIndex==0:
                return [1]
            elif rowIndex==1:
                return [1,1]
            a = [1,1]
            for j in range(rowIndex-1):
                b = []
                b.append(1)
                for i in range(len(a)-1):
                    s = a[i]+a[i+1]
                    b.append(int(s))
                b.append(1)
                a = b
            return b