"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        heap = []
        output = 0

        for interval in intervals:
            # Free as many rooms as possible
            while heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, interval.end)
            output = max(output, len(heap))

        return output
