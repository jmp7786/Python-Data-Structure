
class Simple_list:
    head = None
    size = 0
    class Node:
        next = None
        key = None
        
        def __init__(self, key, next=None):
            self.next = next
            self.key = key
            
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return len(self.size) <= 0
    
    def insert_front(self, key):
        self.head = self.Node(key, next=self.head)
        self.size += 1
        
    def insert_after(self, key, p):
        p.next = self.Node(key, next=p.next)
        self.size += 1
        
    def search(self, key):
        target = self.head
        
        for i in range(self.size):
            if target.key == key:
                return i
            
            target = target.next
        
        return None
    
    def delete_front(self):
        self.head = self.head.next
        self.size -= 1
        
    def delete_after(self, p):
        p.next = p.next.next
        self.size -= 1
        
    def print_list(self):
        target = self.head
        
        for i in range(self.size):
            print(target.key, end=' ')
            target = target.next
        print()
        
            