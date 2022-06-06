class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # for i in range(len(envelopes)):
        #     envelopes[i][1] = -envelopes[i][1]
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        arr = []
        for a,b in envelopes:
            if not arr:
                arr.append((a,b))
            else:
                if arr[-1][0]<a and arr[-1][1]<b:
                    arr.append((a,b))
                else:
                    l = 0
                    r = len(arr) - 1
                    while l<r:
                        mid = (l+r)//2
                        if arr[mid][1]<b:
                            l = mid + 1
                        else:
                            r = mid
                    arr[l] = (a,b)
        return len(arr)