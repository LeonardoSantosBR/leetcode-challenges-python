class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_map = {} #*hash map
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1

        result = []
        limit = len(nums) / 3
        for num, count in num_map.items():
          if count > limit:
            result.append(num)
        return result

solution = Solution()
print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([2,2]))

# • Sua solução: O(n) tempo — O(n) espaço.
# • Sugerido: O(n) tempo — O(1) espaço, via Boyer-Moore para 2 candidatos.