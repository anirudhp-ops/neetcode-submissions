class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count, s2Count = [0] * 26, [0] * 26

        if len(s1) > len(s2): 
            return False
        
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        first = 0
        second = len(s1)

        while second <= len(s2):
            if s1Count == s2Count:
                return True
            if second == len(s2):
                break
            s2Count[ord(s2[second]) - ord('a')] += 1
            s2Count[ord(s2[first]) - ord('a')] -= 1
            first += 1
            second += 1

        return False
