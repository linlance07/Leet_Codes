class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = []
        n = len(nums)
        for i in nums:
            if st:
                if len(st)==1:
                    st.append(i)
                else:
                    if st[-1]==st[-2]==i:
                        n -= 1
                        continue
                    st.append(i)
            else:
                st.append(i)
        nums[:] = st
        return n