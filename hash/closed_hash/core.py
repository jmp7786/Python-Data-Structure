class Node:
    def __init__(self, key, item, next):
        self.key = key
        self.item = item
        self.next = next
    
    
class Chaining:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
    
    def hash(self, key):
        return key % self.size

    def put(self, key, item):
        i = self.hash(key)
        p = self.array[i]
        
        while p != None:
            if p.key == key:
                p.item = item
                return
            
            p = p.next
        
        self.array[i] = Node(key, item, self.array[i])
        
    def get(self, key):
        i = self.hash(key)
        p = self.array[i]
        
        while p != None:
            if p.key == key:
                return p.item
            
            p = p.next
        
        return None
    
    def get_attributes(self):
        results = list()
        
        for i in range(self.size):
            results.append(list())
            p = self.array[i]
            
            while p != None:
                results[i].append([p.key, p.item])
                p = p.next
            
        return results
        