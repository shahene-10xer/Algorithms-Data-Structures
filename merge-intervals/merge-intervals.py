class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        
        sort intervals based on a.start
        -- -__ -_-
        start = interval[0][0]
        end = interval[0][1]
        if b.start <= a.end:
            --overlapping 
            end = max(a.end, b.end)
        else:
            --non-overlapping
            append to merged_intervals(start, end) previous overlapping interval
            start = b.start
            end = b.end
        append last interval to merged_intervals
        
        return merged_intervals
        
        '''
        intervals.sort(key = lambda x: x[0])
        merged_intervals = []
        
        a_start = intervals[0][0]
        a_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            b_start, b_end = intervals[i][0], intervals[i][1]
            if b_start <= a_end:
                a_end = max(a_end, b_end) # overlapping
            else:
                merged_intervals.append([a_start, a_end])
                a_start, a_end = intervals[i][0], intervals[i][1]
        merged_intervals.append([a_start, a_end])
        
        return merged_intervals
        