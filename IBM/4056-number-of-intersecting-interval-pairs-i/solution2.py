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


#   line 4
#   starts = []
#   for s, _ in intervals:
#       starts.append(s)
#   -for s, _ in intervals percorre a lista intervals. Cada elemento é um par [start, end], e o Python desempacota 
#   o par em duas variáveis: s recebe o primeiro valor (o início), _ recebe o segundo (o fim).
#   -_ significa “vou receber esse valor, mas não pretendo usá-lo”
#   
#
#   line 18   
#   for i in range(len(intervals)):
#       start, e = intervals[i]
#   -for i, (_, e) in enumerate(intervals): pega o índice de cada intervalo e já separa o intervalo em início e fim.
#   -para cada intervalo upper_bound devolve o indice cujo start é maior que o fim de target
#    
#   line 20 
#   -soma ao total quantos intervalos cruzam com o intervalo atual i e que vêm depois dele na lista ordenada.
#