class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() #*two pointers*

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            ar = [int(digit) for digit in str(n)]

            left = 0
            right = len(ar) - 1
            s = 0

            while left < right:
                s += ar[left] ** 2 + ar[right] ** 2
                left += 1
                right -= 1

            if left == right:
                s += ar[left] ** 2

            n = s

        return True


solution = Solution()
print(solution.isHappy(2))   # False
print(solution.isHappy(19))  # True
