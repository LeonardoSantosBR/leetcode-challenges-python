class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map= {} #*hash map*
        for i in range(len(nums)):
            if target - nums[i] in num_map:
                return [num_map[target - nums[i]], i]
            num_map[nums[i]] = i
        return []

solution = Solution();
solution.twoSum([12,9,6,12], 15)
solution.twoSum([2,7,11,15], 9)
solution.twoSum([3,2,4], 6)