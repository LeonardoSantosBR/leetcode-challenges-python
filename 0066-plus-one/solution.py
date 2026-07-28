class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1, -1): #*array*
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
            
        
solution = Solution();
solution.plusOne([1,2,3]);
solution.plusOne([9,9,9]);