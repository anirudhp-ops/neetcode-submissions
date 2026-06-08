from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        frq = defaultdict(int)
        new_s = ""

        for char in s: 
            frq[char] += 1 
        
        for char in order: 
           
            if char in frq: 
                for i in range(0, frq[char]): 
                    new_s += char
                frq[char] = 0 
        
        for letter in frq: 
            for i in range(0, frq[letter]): 
                new_s += letter
        
        return new_s


            



        