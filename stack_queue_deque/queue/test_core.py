from stack_queue_deque.queue.core import Queue

 

def test_core():
    q = Queue()

    q.add('apple')
    assert q.get_attributes() == ['apple']
    
    q.add('pear')
    assert q.get_attributes() == ['apple', 'pear']
    
    q.add('mango')
    assert q.get_attributes() == ['apple', 'pear', 'mango']
    q.add('orange')
    assert q.get_attributes() == ['apple', 'pear', 'mango', 'orange']
    
    q.remove()
    assert q.get_attributes() == ['pear', 'mango', 'orange']
    q.remove()
    assert q.get_attributes() == ['mango', 'orange']
    q.remove()
    assert q.get_attributes() == ['orange']
    
    q.remove()
    assert q.get_attributes() == []

    print('----------------------------------------------------------------------')
    # gc reference counting test
    q.add('apple')
    q.add('pear')
    q.remove()
    q.remove()

    # assert q.get_attributes() == 1

if __name__ == "__main__":
    test_core()