class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        back = 0
        ss = ""
        for i in range(len(s)-1,-1,-1):
            if s[i]=='#':
                back += 1
            else:
                if back:
                    back -= 1
                else:
                    ss = s[i] + ss
        back = 0
        tt = ""
        for i in range(len(t)-1,-1,-1):
            if t[i]=='#':
                back += 1
            else:
                if back:
                    back -= 1
                else:
                    tt = t[i] + tt
        if ss==tt:
            return True
        return False
                    
            