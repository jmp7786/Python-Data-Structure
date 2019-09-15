class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next


class SimpleList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_front(self, k):
        self.head = Node(k, self.head)
        self.size += 1
    
    def insert_after(self, k, n):
        n.next = Node(k, n.next)
        self.size += 1
    
    def search(self, key):
        t = self.head
        
        for i in range(self.size):
            if t.key == key:
                return i
            
            t = t.next
        
        return None
    
    def delete_front(self):
        self.head = self.head.next
        self.size -= 1
    
    def delete_after(self, n):
        n.next = n.next.next
        self.size -= 1
    
    def get_attributes(self):
        results = list()
        t = self.head
        
        for i in range(self.size):
            results.append(t.key)
            t = t.next
        
        return results