"""
# deque은 Double Ended Queue의 구현체이며, 양쪽에서 데이터를 넣거나 꺼낼 수 있다.
"""
from collections import deque

# 큐를 구현하기위해서는 한 방향에서 넣고, 반대 방향에서 꺼내야한다.
class Deque(deque):
    # push를 override 한다.
    def enqueue(self, x):
       super().append(x) # 오른쪽에서 데이터를 enqueue 한다.
    
    def dequeue(self):
       super().popleft()  # 왼쪽에서 데이터를 dequeue 한다.
    
    def display(self):
        result = list()
        for node in self.__iter__():
            result.append(node)
        
        return result
         
         
         

