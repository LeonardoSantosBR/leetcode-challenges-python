class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = [""] * len(words)
        for w in words:
          res[int(w[-1]) - 1] = w[:-1]
        return " ".join(res)
        
solution = Solution()
solution.sortSentence("is2 sentence4 This1 a3")

# • Sua solução: O(n) tempo — O(n) espaço, via posicionamento direto.
# • Sugerido: O(n) tempo — O(n) espaço. Já é o ótimo.
