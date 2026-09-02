

class Node: 
    def __init__(self, key: int, value: int): 
        self.key = key
        self.value = value 

        prev = None
        next = None 
    

    



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.Cache = defaultdict()
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:

        if key in self.Cache: 
            self.remove(self.Cache[key])
            self.insert(self.Cache[key])
            return self.Cache[key].value
        return -1 

        

    def put(self, key: int, value: int) -> None:
        if key in self.Cache: 
            self.remove(self.Cache[key])
        self.Cache[key] = Node(key, value)
        self.insert(self.Cache[key])

        

        
        if len(self.Cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.Cache[lru.key]
        
