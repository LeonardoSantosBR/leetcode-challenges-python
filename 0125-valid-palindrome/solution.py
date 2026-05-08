import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = re.sub(r'[\W_]', '', s.lower())
        s2 = re.sub(r'[\W_]', '', s[::-1].lower())
        return s1 == s2;

solution = Solution();
solution.isPalindrome("A man, a plan, a canal: Panama");
solution.isPalindrome("race a car");
