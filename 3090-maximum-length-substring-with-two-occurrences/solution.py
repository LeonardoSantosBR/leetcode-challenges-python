class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l,r= 0,0 #*two pointers*
        _max= 1
        counter= {} #*hash map*
        
        counter[s[0]] = 1
        
        while r < len(s) - 1: #*sliding window*
            r+= 1
            if counter.get(s[r]):
                counter[s[r]]+= 1
            else:
                counter[s[r]]= 1
            
            while counter[s[r]] == 3:
                counter[s[r]] -= 1
                l += 1
            _max = max(_max, r-l+1)
        return _max
        
        
        
solution = Solution()
solution.maximumLengthSubstring("bcbbbcba")