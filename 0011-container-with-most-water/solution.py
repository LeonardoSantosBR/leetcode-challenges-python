class Solution:
    def maxArea(self, height: List[int]) -> int:
        area= 0 #*two pointers* TLE
        
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                new_area = min(height[i],height[j]) * (j-i)
                if new_area>area: area=new_area
        return area
        
solution = Solution()
solution.maxArea([1,8,6,2,5,4,8,3,7])
solution.maxArea([1,1])