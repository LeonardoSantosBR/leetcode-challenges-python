class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:        
        l,r = 0,1 #*sliding window* TLE
        
        while l < len(nums) - 1:
            if r >= len(nums):
                l+=1
                r=l+1  
                continue  
            if nums[l] == nums[r] and r-l <=k: 
                return True
            r+=1
        return False
    
solution = Solution()
solution.containsNearbyDuplicate([1,2,3,1],3)
solution.containsNearbyDuplicate([1,0,1,1],1)
solution.containsNearbyDuplicate([1,2,3,1,2,3],2)