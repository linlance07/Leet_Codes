class Solution:
    def intervalIntersection(self, one: List[List[int]], two: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        while i<len(one) and j<len(two):
            st1,en1 = one[i]
            st2,en2 = two[j]
            if st2<=en1 and en2>=en1:
                ans.append([max(st2,st1),en1])
                i += 1
            elif st1<=en2 and en1>=en2:
                ans.append([max(st1,st2),en2])
                j += 1
            else:
                if st1<st2:
                    i += 1
                elif st2<st1:
                    j += 1
                else:
                    i += 1
                    j += 1
        return ans
                    
            