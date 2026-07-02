from collections import defaultdict


class TimeMap:

    def __init__(self):
        
        self.d = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.d[key][timestamp] = value 

        

    def get(self, key: str, timestamp: int) -> str:
        
        
        if key not in self.d: 
            return ""
        elif timestamp in self.d[key]: 
            return self.d[key][timestamp]
        else: 
            valid = [t for t in self.d[key] if t <= timestamp]
            if not valid:
                return ""
            val = max(valid)
            return self.d[key][val]
       
        
