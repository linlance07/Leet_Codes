class Solution(object):
    def spiralOrder(self, mat):
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        n=len(mat)
        m=len(mat[0])
        ans=[]
        ind=0
        x=0
        y=0
        for i in range(n*m):
            ans.append(mat[x][y])
            mat[x][y]='a'
            a=x+d[ind][0]
            b=y+d[ind][1]
            if a<0 or a>=n or b<0 or b>=m or mat[a][b]=='a':
                ind+=1
                ind%=4
                a=x+d[ind][0]
                b=y+d[ind][1]
            x=a
            y=b
        return ans
                
                
                
            
            
            
        
        