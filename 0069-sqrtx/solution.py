class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0 #*binary search*
        
        left , right = 1 , x
        while left <= right:
            mid = int(left + right) // 2
            sr = mid * mid
            if sr == x:
                return mid
            elif sr < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
        
solution = Solution();
solution.mySqrt(8);