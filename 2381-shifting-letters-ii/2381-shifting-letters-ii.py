class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = []
        for i in s:
            arr.append(ord(i)-97)
        #print(arr)
        n = len(arr)
        D = [0 for i in range(0 , n + 1)]
        D[0] = arr[0]
        for i in range(1,n):
            D[i] = arr[i] - arr[i-1]
        for l,r,s in shifts:
            if s==0:
                s = -1
            D[l] = (D[l]+s)%26
            D[r+1] = (D[r+1]-s)%26
        for i in range(n):
            if i==0:
                arr[i] = D[i]
                continue
            arr[i] = (arr[i-1] + D[i])%26
        ans = ""
        #print(arr)
        for i in arr:
            ans += chr(i+97)
        return ans