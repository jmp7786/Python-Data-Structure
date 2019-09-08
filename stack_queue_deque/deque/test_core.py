from stack_queue_deque.deque.core  import Deque

def test_core():
    q = Deque()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    assert q.get_attributes() == [1,2,3,4]
    
    q.dequeue()
    assert q.get_attributes() == [2,3,4]
    
    q.pop()
    assert q.get_attributes() == [2,3]
    