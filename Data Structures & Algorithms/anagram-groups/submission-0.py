class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs: 
            wordlist = sorted(word) 
            comparer = ''.join(wordlist)
            if comparer not in group:
                group[comparer] = []
            group[comparer].append(word)
        
        lister = []
        counter = 0
        for key in group: 
            
            lister.append(group[key])
            counter += 1 
        
        return lister 