class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return digits[::-1][0] + 1
            
solution = Solution();
solution.plusOne([1,2,3]);