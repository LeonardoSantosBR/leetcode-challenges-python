class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle) #*two pointers*

        for left in range(h - n + 1):
            j = 0
            while j < n and haystack[left + j] == needle[j]:
                j += 1
            if j == n:
                return left

        return -1

solution = Solution()
solution.strStr("hello", "ll")
solution.strStr("sadbutsad", "sad")
solution.strStr("leetcode", "leeto")
solution.strStr("a", "a")