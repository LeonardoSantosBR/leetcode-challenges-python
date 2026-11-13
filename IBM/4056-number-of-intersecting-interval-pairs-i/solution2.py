class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort() #binary search
        starts = [s for s, _ in intervals]
        n = len(starts)

        def upper_bound(target: int) -> int:
            lo, hi = 0, n
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if starts[mid] > target:
                    hi = mid                  
                else:
                    lo = mid + 1             
            return lo

        count = 0
        for i, (_, e) in enumerate(intervals):
            idx = upper_bound(e)
            count += idx - (i + 1)
        return count

solution = Solution()
solution.countIntersectingIntervals(intervals=[[1,2],[2,3],[3,4]])
solution.countIntersectingIntervals(intervals=[[1,5],[2,4],[3,6]])
solution.countIntersectingIntervals(intervals=[[1,2],[3,4],[5,6]])


# Explicação dos trechos principais:
#
# `starts` guarda apenas os inícios dos intervalos. Como os intervalos estão
# ordenados, essa lista pode ser usada pela busca binária.
#
# Em `for s, _ in intervals`, cada intervalo é desempacotado em duas variáveis:
# `s` recebe o início e `_` recebe o fim. O `_` indica que esse valor não será
# utilizado nesse trecho.
#
# `enumerate(intervals)` fornece o índice `i` e o intervalo atual. O padrão
# `(_, e)` ignora o início e guarda apenas o fim em `e`.
#
# Para cada intervalo, `upper_bound(e)` encontra a primeira posição cujo início
# é maior que `e`. Assim, os intervalos entre `i + 1` e essa posição intersectam
# o intervalo atual. Essa quantidade é adicionada a `count`.
#
# Linha 20 soma ao total quantos intervalos cruzam com o intervalo atual i e que 
# vêm depois dele na lista ordenada.
