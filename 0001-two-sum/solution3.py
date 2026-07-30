class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i,j]

solution = Solution();
solution.twoSum([20,71,6,12], 18)
solution.twoSum([2,7,11,15], 9)
solution.twoSum([3,2,4], 6)