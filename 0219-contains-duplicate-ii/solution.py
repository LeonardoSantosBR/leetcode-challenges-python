class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:        
        for i in range(len(nums)): # TLE
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and j-i <= k:
                    return True
        return False
            
        
solution = Solution()
solution.containsNearbyDuplicate([1,2,3,1],3)
solution.containsNearbyDuplicate([1,0,1,1],1)
solution.containsNearbyDuplicate([1,2,3,1,2,3],2)