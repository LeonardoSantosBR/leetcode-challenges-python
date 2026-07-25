class Solution:
    def maxProduct(self, n: int) -> int:
       ar = [int(digit) for digit in str(n)] #*two pointers*
       
       left = 0
       right = left + 1
       maxProduct = 0
            
       for left in range(len(ar)):
        for right in range(left + 1, len(ar)):
         maxProduct = max(maxProduct, ar[left] * ar[right])
         
       return maxProduct
                
            
solution = Solution()
solution.maxProduct(31)
solution.maxProduct(124)
solution.maxProduct(267)
solution.maxProduct(20)
solution.maxProduct(437)