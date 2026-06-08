class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        s1_new = sorted(s1)

        first = 0
        second = len(s1)

        while second <= len(s2): 
            s2_new = sorted(s2[first:second])
            if s1_new == s2_new: 
                return True
            first += 1
            second += 1
        
        return False 
