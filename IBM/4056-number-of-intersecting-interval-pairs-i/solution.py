class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n= len(intervals)
        count= 0
        
        for i in range(n):
            for j in range(i+1, n):
                s1,e1= intervals[i]
                s2,e2= intervals[j]
                
                if e1 >= s2 and e2 >= s1:
                    count += 1
        return count

solution = Solution()
solution.countIntersectingIntervals(intervals=[[1,2],[2,3],[3,4]])
solution.countIntersectingIntervals(intervals=[[1,5],[2,4],[3,6]])
solution.countIntersectingIntervals(intervals=[[1,2],[3,4],[5,6]])

# dois intervalos se cruzam quando o fim de cada um é maior ou igual ao começo do outro
# e o fim do segundo é maior ou igual ao o inicio do primeiro(engloba) 