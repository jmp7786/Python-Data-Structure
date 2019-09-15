class Node:
    def __init__(self, item, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0
    
    def insert_after(self, p, item):
        n = Node(item, p, p.next)
        p.next.prev = n
        p.next = n
        
        self.size += 1
    
    def insert_before(self, p, item):
        n = Node(item, p.prev, p)
        p.prev.next = n
        p.prev = n
        
        self.size += 1
    
    def delete(self, p):
        p.next.prev, p.prev.next = p.prev, p.next
        self.size -= 1
    
    def get_attributes(self):
        result = list()
        if self.size != 0:
            p = self.head.next
            for i in range(self.size):
                result.append(p.item)
                p = p.next
        return result



