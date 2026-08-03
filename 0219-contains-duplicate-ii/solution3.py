class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:        
        nm={} #*hash map*
        for i, v in enumerate(nums):
            if v in nm and i - nm[v] <=k: return True
            nm[v]= i
        return False
    
solution = Solution()
solution.containsNearbyDuplicate([1,2,3,1],3)
solution.containsNearbyDuplicate([1,0,1,1],1)
solution.containsNearbyDuplicate([1,2,3,1,2,3],2)