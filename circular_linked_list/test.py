from circular_linked_list.imploment import CList
from circular_linked_list.imploment2 import CircularLinkedList

if __name__ == '__main__':
    # s = CList()
    s = CircularLinkedList()
    
    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple')
    s.get_list()
    print('s의 길이 =', s.size)
    print('s의 첫 항목 :', s.first())
    s.delete()
    print('첫 노드 삭제 후: ', end='')
    s.get_list()
    print('s의 첫 길이 =', s.size)
    print('s의 첫 항목 :', s.first())
    s.delete()
    print('첫 노드 삭제 후: ', end='')
    s.get_list()
    s.delete()
    print('첫 노드 삭제 후: ', end='')
    s.get_list()
    s.delete()
    print('첫 노드 삭제 후: ', end='')
    s.get_list()
    
def test_circular_linked_list():
    c = CircularLinkedList()
    c.insert('pear')
    assert c.get_list() == ['pear','1']