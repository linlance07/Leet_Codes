class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        ans = ""
        act = 0
        for i in s:
            if i=='6':
                if act:
                    ans+='6'
                else:
                    ans+='9'
                    act = 1
            else:
                ans+='9'
        return int(ans)
                    