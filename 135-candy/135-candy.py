class Solution:
    def candy(self, R: List[int]) -> int:
        arr = [1]*len(R)
        for i in range(1,len(R)):
            if R[i]>R[i-1] and arr[i]<=arr[i-1]:
                arr[i] = arr[i-1] + 1
        for i in range(len(R)-2,-1,-1):
            if R[i]>R[i+1] and arr[i]<=arr[i+1]:
                arr[i] = arr[i+1] + 1
        return sum(arr)