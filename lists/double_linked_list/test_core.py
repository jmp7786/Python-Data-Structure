from lists.double_linked_list.core import DoublyLinkedList

def test_core():
        s = DoublyLinkedList()
        s.insert_after(s.head, 'apple')
        assert s.get_attributes() == ['apple']
        
        s.insert_before(s.tail, 'orange')
        assert s.get_attributes() == ['apple', 'orange']
        
        s.insert_before(s.tail, 'cherry')
        assert s.get_attributes() == ['apple', 'orange', 'cherry']
        
        s.insert_after(s.head.next, 'pear')
        assert s.get_attributes() == ['apple', 'pear', 'orange', 'cherry']
        
        print('마지막 노드 삭제 후 ')
        s.delete(s.tail.prev)
        assert s.get_attributes() == ['apple', 'pear', 'orange']
        
        print('맨 끝에 포도 삽입 후')
        s.insert_before(s.tail, 'grape')
        assert s.get_attributes() == ['apple', 'pear', 'orange', 'grape']
        
        print('첫 노드 삭제 후')
        s.delete(s.head.next)
        assert s.get_attributes() == ['pear', 'orange', 'grape']
        
        print('첫 노드 삭제 후')
        s.delete(s.head.next)
        assert s.get_attributes() == ['orange', 'grape']
        
        print('첫 노드 삭제 후')
        s.delete(s.head.next)
        assert s.get_attributes() == ['grape']
        
        print('첫 노드 삭제 후')
        s.delete(s.head.next)
        assert s.get_attributes() == []
        
        