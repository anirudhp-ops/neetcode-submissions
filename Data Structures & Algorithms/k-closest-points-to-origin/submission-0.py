import math 
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        heap = []
        for item in points: 
            val = math.sqrt((item[0] ** 2) + (item[1] ** 2))
            
            heapq.heappush(heap, [-val, item[0], item[1]]) 
            if len(heap) > k: 
                heapq.heappop(heap) 
        
        while heap: 
            val = heapq.heappop(heap)
            res.append( [val[1], val[2]] ) 
                

        return res