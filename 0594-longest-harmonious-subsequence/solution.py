class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort() #*sliding window*
        l=0
        _max=0
        
        for i in range(len(nums)):
            while nums[i] - nums[l] > 1: 
                l+=1
            if nums[i] - nums[l] == 1: 
                _max = max(_max, i-l+1)
        return _max    
            
        
solution = Solution()
solution.findLHS([1,3,2,2,5,2,3,7])