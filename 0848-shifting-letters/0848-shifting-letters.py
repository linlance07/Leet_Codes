class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = ""
        arr = []
        for i in s:
            arr.append(ord(i)-97)
        Q = [shifts[-1]]*len(s)
        for i in range(len(shifts)-2,-1,-1):
            Q[i] = shifts[i] + Q[i+1]
        for i in range(len(s)):
            ans += chr(((arr[i]+Q[i])%26)+97)
        return ans