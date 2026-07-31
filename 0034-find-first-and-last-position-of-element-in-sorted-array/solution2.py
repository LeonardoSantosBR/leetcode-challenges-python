class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(first: bool) -> int:
            lo, hi, ans = 0, len(nums) - 1, -1 #*binary search*

            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    ans = mid
                    if first:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans
        
        return [search(True), search(False)]


solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))   
print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))   
print(solution.searchRange([], 0))                    
print(solution.searchRange([8, 8, 8], 8))          