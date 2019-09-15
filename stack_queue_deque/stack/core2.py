class Stack:
    head = None
    
    class Node:
        def __init__(self, key, next=None):
            self.key = key
            self.next = next
            
    def push(self, key):
        self.head = self.Node(key, self.head)
        
    def pop(self):
        _head = self.head
        self.head = self.head.next
        
        return _head.key
    
    def peek(self):
        return self.head.key
    
    