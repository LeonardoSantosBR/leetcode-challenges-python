class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1: return False
        num_map = {} #*hash map
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
            if num_map[num] == 2:
                return True

        return False
        
solution = Solution()
solution.containsDuplicate([1,2,3,4])

# • Sua solução: O(n) tempo — O(n) espaço.
# • Sugerido: O(n) tempo — O(n) espaço, via set (teste de pertinência).