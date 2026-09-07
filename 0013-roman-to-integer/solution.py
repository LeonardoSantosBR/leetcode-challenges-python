class Solution:
    def romanToInt(self, s: str) -> int:
        rn={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} #*hash map
        n=0
        
        for i in range(len(s)-1):
            if rn[s[i]] < rn[s[(i+1)]]:
                n-= rn[s[i]]
            else:
                n+= rn[s[i]]
        return n+rn[s[-1]]

solution = Solution();
solution.romanToInt("III")
solution.romanToInt("LVIII")
solution.romanToInt("MCMXCIV")