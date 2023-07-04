#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        ans = 0
        l = r = 0
        p = 1
        while r<n:
            x = a[r]
            p *= x
            while l<=r and p>=k:
                p = p // a[l]
                l += 1
            ans += r - l + 1
            r += 1
        return ans
                
            
    
    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends