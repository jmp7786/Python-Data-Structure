class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next
        

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
    
    def insert_after(self, n, k):
        t = Node(k, n, n.next)
        n.next.prev = t
        n.next = t
        
        self.size += 1
    
    def insert_before(self, n, k):
        t = Node(k, n.prev, n)
        n.prev.next = t
        n.prev = t
        
        self.size += 1
    
    def delete(self, n):
        n.next.prev, n.prev.next = n.prev, n.next
        self.size -= 1
    
    def get_attributes(self):
        results = list()
        t = self.head.next
        for i in range(self.size):
            results.append(t.key)
            t = t.next
        
        return results
        