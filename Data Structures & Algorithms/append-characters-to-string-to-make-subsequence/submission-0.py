class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first = 0
        second = 0 
        while first < len(s) and second < len(t): 
            if s[first] == t[second]: 
                first += 1
                second += 1 
            else: 
                first += 1 
        
        return len(t) - second
        