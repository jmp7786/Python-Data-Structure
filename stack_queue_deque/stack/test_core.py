
from stack_queue_deque.stack.core import Stack

def test_core():
    s = Stack()

    s.push(1)
    assert s.peek() == 1
    
    s.push(2)
    assert s.peek() == 2
    
    s.push(3)
    assert s.peek() == 3
    
    s.push(4)
    assert s.peek() == 4
    
    s.push(5)
    assert s.peek() == 5
    
    count = 5
    while s.head:
        assert s.pop() == count
        count -= 1
    