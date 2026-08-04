class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0 #*two pointers* *begin and end of answer*
        
        def expand(left,right) -> None:
            nonlocal start, max_len #nonlocal write within the scope of the enclosing function
            while left>=0 and right<len(s) and s[left]==s[right]: #*expand around the center*
                left-=1
                right+=1
            length = right-left-1 #end - begin - 1
            if length>max_len:
                max_len=length #write start,max_len in the outer scope
                start=left+1  #same
            
        for i in range(len(s)):
            expand(i,i) #odd
            expand(i,i+1) #even
        return s[start:start+max_len]
        
solution = Solution()
solution.longestPalindrome("babad")
solution.longestPalindrome("cbbd")