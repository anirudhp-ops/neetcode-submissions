import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for val in nums: 

            if val not in freq:
                freq[val] = 0
            freq[val] += 1

        heap = []

        for num, count in freq.items(): 
            heapq.heappush(heap, (count, num))

            if len(heap) > k: 
                heapq.heappop(heap)
            
        result = []
        for count, num in heap:
            result.append(num)
        return result


        


        