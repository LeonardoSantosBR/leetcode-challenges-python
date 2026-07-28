class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) - 1 #*binary search*
        
        while left <= right:
            mid = int(left + right) // 2
            if(nums[mid] == target):
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]: # right ordered
                    right = mid - 1
                else:
                    left = mid + 1
            else: # left ordered
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            
solution = Solution();
solution.search([4,5,6,7,0,1,2], 0);
solution.search([4,5,6,7,0,1,2], 5);
solution.search([10,11,12,0,1,2,3], 1);