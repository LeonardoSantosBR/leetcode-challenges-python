import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0 #*min-heap* 
        intervals.sort(key=lambda interval: interval[0])

        heap = []

        for begin, end in intervals:
            if heap and heap[0] <= begin:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)


solution = Solution()
solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
solution.minMeetingRooms([[7, 10], [2, 4]])