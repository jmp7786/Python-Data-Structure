class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
        

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def add(self, item):
        if self.front == None:
            n = Node(item)
            self.front = n
            self.rear = n
        else:
            self.rear.next = Node(item)
            self.rear = self.rear.next
    
    def remove(self):
        if self.front == None:
            return None
        else:
            result = self.front.item
            self.front = self.front.next
            
            return result
    
    def get_attributes(self):
        results = list()
        target = self.front
        
        while target != None:
            results.append(target.item)
            target = target.next
        
        return results
        
    