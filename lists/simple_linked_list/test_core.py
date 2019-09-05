from lists.simple_linked_list.core import SimpleList

def test_circular_linked_list():
    s = SimpleList()
    s.insert_front('orange')
    assert s.get_attributes() == ['orange']
    
    s.insert_front('apple')
    assert s.get_attributes() == ['apple', 'orange']
    
    s.insert_after('cherry', s.head.next)
    assert s.get_attributes() == ['apple', 'orange', 'cherry']
    
    s.insert_front('pear')
    assert s.get_attributes() == ['pear', 'apple', 'orange', 'cherry']

    assert s.search('cherry') == 3

    s.delete_after(s.head)
    assert s.get_attributes() == ['pear', 'orange', 'cherry']

    s.delete_front()
    assert s.get_attributes() == ['orange', 'cherry']

    s.insert_front('mango')
    s.insert_front('strawberry')

    assert s.get_attributes() == ['strawberry', 'mango', 'orange', 'cherry']
    
    s.delete_after(s.head.next.next)
    assert s.get_attributes() == ['strawberry', 'mango', 'orange']
    
    
    