class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_map= {} #*hash map*
        for n in nums:
            if n not in num_map: 
                num_map[n] = 1
            else:
                num_map[n] += 1
        
        for l in num_map.items():
            if l[1] != 2: return l[0]
            
        
solution = Solution()
solution.singleNumber([2,2,1])
solution.singleNumber([4,1,2,1,2])