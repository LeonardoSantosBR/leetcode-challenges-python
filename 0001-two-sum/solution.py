class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
          for j, y in enumerate(nums[i + 1:], start=i+1):
            s = n + y
            if s == target:
                result = [i, j]
                return result
            
solution = Solution();
solution.twoSum([2,7,11,15], 9)
