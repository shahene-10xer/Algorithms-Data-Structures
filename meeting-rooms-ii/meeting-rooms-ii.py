class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        # return minimum number of conference rooms required
        
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2
        sort based on interval start time
        if interval_i+1 starts before interval_i-1 ends:
            overlapping intervals so only add 1 room 
        non-overlapping intervals would get 1 room on their own as well
        '''
        intervals.sort(key = lambda x: x[0])
        min_heap = []
        
        heapq.heappush(min_heap, intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
        
        return len(min_heap)
