class Node:
    def __init__(self, key, data, next):
        self.key = key
        self.data = data
        self.next = next
    

class Chaining:
    def __init__(self, size):
        self.M = size
        self.a = [None] * size
        
    def hash(self, key):
        return  key % self.M
    
    def put(self, k, d):
        i = self.hash(k)
        p = self.a[i]
        
        while p != None:
            if k == p.key:
                p.data = d
                return
            p = p.next
        
        self.a[i] = Node(k, d, self.a[i])
    
    def get(self, k):
        i = self.hash(k)
        p = self.a[i]
        
        while p != None:
            if k == p.key:
                return p.data
            p = p.next
        
        return None
    
    def get_attributes(self):
        results = list()
        
        for i in range(self.M):
            results.append(list())
            p = self.a[i]
            while p != None:
                results[i].append([p.key, p.data])
                p = p.next
            
        
        return results
        
        
        