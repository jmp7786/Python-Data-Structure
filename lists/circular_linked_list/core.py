class Node:
    def __init__(self, k, next=None):
        self.key = k
        self.next = next
    

class CircularLinkedList:
    def __init__(self):
        self.last = None
        self.size = 0
    
    def insert(self, k):
        if self.size == 0:
            self.last = Node(k)
            self.last.next = self.last
        else:
            self.last.next = Node(k, self.last.next)
            
        self.size += 1
    
    def first(self):
        return self.last.next.key
    
    def delete(self):
        if self.size == 0:
            return None
        
        if self.size == 1:
            self.last.next = None
            self.last = None
        
        else:
            self.last.next = self.last.next.next
        
        self.size -= 1
    
    def get_attributes(self):
        results = list()
        t = self.last
        
        for i in range(self.size):
            results.append(t.next.key)
            t = t.next
        
        return results
        