class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        
        container = defaultdict(list)

        


        for val in strs: 
            count = [0] * 26  
            for c in val: 
                count[ord(c) - ord('a')] += 1 
            
            c = tuple(count)
            container[c].append(val)


        return list(container.values())

