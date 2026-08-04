class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,max_area= 0,len(height)-1,0 #*two pointers* 
        
        while l < r:
            new_area = min(height[l],height[r]) * (r-l)
            if new_area > max_area: max_area=new_area
            if height[l] < height[r]:
                l+= 1
            else:
                r-= 1
        return max_area
        
solution = Solution()
solution.maxArea([1,8,6,2,5,4,8,3,7])
solution.maxArea([1,1])