class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split() #*bubble sort* *string*
        for _ in s:
            for i in range(len(s) - 1):
                if s[i][len(s[i]) - 1] > s[i+1][len(s[i+1]) - 1]:   
                    s[i], s[i+1] = s[i+1], s[i]
                    
        for i in range(len(s)): 
            s[i] = s[i].replace(s[i][len(s[i]) - 1], "")
        return " ".join(s)
        
solution = Solution()
solution.sortSentence("is2 sentence4 This1 a3")