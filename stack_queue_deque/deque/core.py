"""
# deque은 Double Ended Queue의 구현체이며, 양쪽에서 데이터를 넣거나 꺼낼 수 있다.
"""

from collections import deque

class Deque(deque):
    def enqueue(self, x):
       super().append(x)
    
    def dequeue(self):
       super().popleft()
    
    def get_attributes(self):
        result = list()
        for node in self.__iter__():
            result.append(node)
        
        return result
         
         
         

