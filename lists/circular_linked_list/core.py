class CircularLinkedList:
    last = None
    size = 0
    
    class Node:
        def __init__(self, key, next=None):
            self.key = key
            self.next = next
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        return self.last.next.key
    
    def insert(self, key):
        if self.is_empty():
            self.last = self.Node(key)
            self.last.next = self.last
        else:
            self.last.next = self.Node(key, self.last.next)
        
        self.size += 1
    
    def delete(self):
        if self.is_empty():
            return None
        else:
            if self.size == 1:
                self.last.next = None
                self.last = None
            else:
                self.last.next = self.last.next.next
        
        self.size -= 1
    
    def get_list(self):
        lst = list()
        
        if not self.is_empty():
            target = self.last
            for i in range(self.size):
                lst.append(target.next.key)
                target = target.next
        
        return lst
