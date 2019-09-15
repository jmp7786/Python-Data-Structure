class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next
    

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, k):
        self.head = Node(k, self.head)
    
    def pop(self):
        _head = self.head
        self.head = self.head.next
        
        return _head.key
    
    def peek(self):
        return self.head.key
        