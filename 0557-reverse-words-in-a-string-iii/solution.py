class Solution:
    def reverseWords(self, s: str) -> str:
        right= 0 #*two pointers*
        left= 0
        result= ""
        
        while right < len(s):
            if s[right] != ' ':
                right +=1
            else:
                result += s[left:right+1][::-1]
                right += 1
                left = right
        result += ' '
        result += s[left:right][::-1]
        return result[1:]
        
solution = Solution()
solution.reverseWords("Let's take LeetCode contest")

# • Sua solução: O(n²) tempo — O(n) espaço (concatenação de string em loop).
# • Sugerido: O(n) tempo — O(n) espaço, via split + reverse + join.