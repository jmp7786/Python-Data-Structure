class Queue:
    rear = None
    front = None
    
    def __del__(self):
        print('Queue object', id(self))
        pass
    class Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next
            print('created', hex(id(self)))
            
        def __del__(self):
            print('deleted', hex(id(self)))
            pass
    
    def add(self, item):
        if not self.rear:
            self.rear = self.Node(item)
            self.front = self.rear
        else:
            self.rear.next = self.Node(item)
            self.rear = self.rear.next

    def remove(self):
        if not self.front:
            return None
        
        elif not self.front.next:
            
            result = self.front.item
            
            self.rear = None
            self.front = None
            
            return result
        
        else:
            result = self.front.item
            self.front = self.front.next
            
            return result
    
    def get_attributes(self):
        target = self.front
        results = list()
        
        while target:
            results.append(target.item)
            target = target.next
        
        return results
    
    

