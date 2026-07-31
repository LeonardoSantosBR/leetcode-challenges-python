class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_map= {} #*hash map*
        for i in range(len(word)):
            if word[i] not in letter_map:
                letter_map[word[i]] = 1
            else:
                letter_map[word[i]] += 1
        r= 0
        for i, v in enumerate(sorted(letter_map.values(), reverse=True)):
            r += v * (i // 8 + 1)
        return r
        
solution = Solution()
solution.minimumPushes("aabbccddeeffgghhiiiiii")