class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort() #*sliding window*
        l,r=0,0
        _max=0
        
        while r < len(nums)-1:
            r+=1
            while nums[r]-nums[l] > 1:
               l+=1
            if nums[r]-nums[l] == 1:
               _max = max(_max, r-l+1)
        return _max
            
        
solution = Solution()
solution.findLHS([1,3,2,2,5,2,3,7])