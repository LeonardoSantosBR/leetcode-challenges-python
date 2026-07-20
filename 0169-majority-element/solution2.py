class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 #*Boyer-Moore Voting Algorithm*
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
        
solution = Solution();
solution.majorityElement([3,4,4,3,3])