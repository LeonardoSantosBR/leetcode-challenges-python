class Solution:
    def romanToInt(self, s: str) -> int:
        rn={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} #*hash map
        res, prev = 0,0
        
        for i in s[::-1]:
            if rn[i] >= prev:
                res+= rn[i]
            else:
                res-= rn[i]
            prev= rn[i]
        return res
            

solution = Solution();
solution.romanToInt("IV")
solution.romanToInt("III")
solution.romanToInt("LVIII")
solution.romanToInt("MCMXCIV")