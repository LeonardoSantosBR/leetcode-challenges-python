class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} #*hash map*
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

solution = Solution();
solution.twoSum([2,7,11,15], 9)
solution.twoSum([3,2,4], 6)