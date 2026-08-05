class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        intervals.sort()
        res = 0
        first_end = intervals[0][1]


        for start, end in intervals[1:]: 

            if start >= first_end: 
                first_end = end 
            
            else: 
                res += 1 
                first_end = min(end, first_end) 

            
        return res 

