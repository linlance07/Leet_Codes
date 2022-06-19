class Solution:
    def isValid(self, A: str) -> bool:
        st = []
        for i in A:
            if i=='(' or i=='[' or i=='{':
                st.append(i)
            else:
                if not st:
                    return 0
                if i==')':
                    if st[-1]!='(':
                        return 0
                elif i==']':
                    if st[-1]!='[':
                        return 0
                else:
                    if st[-1]!='{':
                        return 0
                st.pop()
        if st:
            return 0
        return 1
                    
                    