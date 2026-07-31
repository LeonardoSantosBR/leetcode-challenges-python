class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi, left = 0, len(nums) - 1, -1 #*binary search* 
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                left = mid
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        if left == -1:
            return [-1, -1]

        lo, hi, right = left, len(nums) - 1, left #*binary search* 
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                right = mid
                lo = mid + 1
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return [left, right]


solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))   
print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))   
print(solution.searchRange([], 0))                    
print(solution.searchRange([8, 8, 8], 8))          