class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        num_map = {} #*hash map*
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
                continue
            num_map[num] += 1
            if num_map[num] > (len(nums) / 2):
                return num
            
solution = Solution();
solution.majorityElement([3,2,3])

# ◦ Sua solução: O(n) tempo — O(n) espaço. 
# ◦ Sugerido: O(n) tempo — O(1) espaço, via Boyer-Moore.