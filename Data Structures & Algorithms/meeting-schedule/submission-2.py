"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        new = []
        for interval in intervals: 
            new.append([interval.start, interval.end])

        new.sort()
        print(new)

        for i in range(0, len(new) - 1 ): 

            if new[i][1] > new[i+1][0]: 
                return False 
        return True 