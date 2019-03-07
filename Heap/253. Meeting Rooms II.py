# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        #edge case
        if not intervals:
            return 0
        #sort by the start time    
        intervals.sort(key = lambda x: x.start)
        freeRooms = []
        #keep a heap of min endtime to check available rooms
        heapq.heappush(freeRooms, intervals[0].end)
        for meet in intervals[1:]:
            if meet.start >= freeRooms[0]:
                heapq.heappop(freeRooms)
            heapq.heappush(freeRooms, meet.end)
        return len(freeRooms)
                
                
# time: O(nlogn)
# space: O(n)


#sort start time and end time separatly. compare the start time with earlist end time
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        #edge case
        if not intervals:
            return 0
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        ans, end = 0, 0
        for start in starts:
            if start < ends[end]:
                ans += 1
            else:
                end += 1
        return ans

                
# time: O(nlogn)
# space: O(n)
