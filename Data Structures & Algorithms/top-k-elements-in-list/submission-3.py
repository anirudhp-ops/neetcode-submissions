import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for val in nums: 
            freq[val] += 1 
        
        heap = []
        for key, val in freq.items(): 
            heapq.heappush(heap, (val, key))
        
            if len(heap) > k: 
                heapq.heappop(heap) 
        
        res = []
        print(heap)
        for val in heap: 
            res.append(val[1])
        
        return res



        