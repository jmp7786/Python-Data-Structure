from lists.circular_linked_list.core import CircularLinkedList

def test_core():
    s = CircularLinkedList()
    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple')
    assert s.get_attributes() == ['apple', 'orange', 'cherry', 'pear']
    s.delete()
    assert s.get_attributes() == ['orange', 'cherry', 'pear']
    assert s.first() == 'orange'
    s.delete()
    assert s.get_attributes() == ['cherry', 'pear']
    s.delete()
    assert s.get_attributes() == ['pear']
    s.delete()
    assert s.get_attributes() == []
    

