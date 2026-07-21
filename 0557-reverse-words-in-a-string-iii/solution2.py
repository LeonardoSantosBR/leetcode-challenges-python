class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))


solution = Solution()
solution.reverseWords("Let's take LeetCode contest")

# • Sua solução: O(n) tempo — O(n) espaço.
# • Sugerido: O(n) tempo — O(n) espaço, via split + reverse + join.