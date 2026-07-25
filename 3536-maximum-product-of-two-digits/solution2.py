class Solution:
    def maxProduct(self, n: int) -> int:
       ar = sorted(int(d) for d in str(n))
       return ar[-1] * ar[-2]   # produto dos dois maiores
                
            
solution = Solution()
solution.maxProduct(31)
solution.maxProduct(124)
solution.maxProduct(267)
solution.maxProduct(20)
solution.maxProduct(437)