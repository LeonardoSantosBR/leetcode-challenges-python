class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1 #*binary search*
        
        while left <= right:
            mid = int(left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
solution = Solution();
solution.searchInsert([1,3,5,6], 5);