from trees.binary_heap.core2 import BinaryHeap

def test_core():
    a = [None] * 1
    
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([50, 'lime'])
    a.append([60, 'mango'])
    a.append([20, 'cherry'])
    a.append([30, 'grape'])
    a.append([35, 'orange'])
    a.append([10, 'apricot'])
    a.append([15, 'banana'])
    a.append([45, 'lemon'])
    a.append([40, 'kiwi'])
    
    
    b = BinaryHeap(a)
    print('힙 만들기 전')
    print(b.get_attributes(), 1)
    assert b.get_attributes() == [[90, 'watermelon'],[80, 'pear'],[70, 'melon'],[50, 'lime'],[60, 'mango'],[20, 'cherry'],[30, 'grape'],[35, 'orange'],[10, 'apricot'],[15, 'banana'],[45, 'lemon'],[40, 'kiwi']]
    
    b.create_heap()
    print('최소힙')
    # print(b.get_attributes())
    assert b.get_attributes() == [[10, 'apricot'], [15, 'banana'], [20, 'cherry'], [35, 'orange'], [45, 'lemon'], [40, 'kiwi'], [30, 'grape'], [80, 'pear'], [50, 'lime'], [60, 'mango'], [90, 'watermelon'], [70, 'melon']]

    
    print('최솟값 삭제 후')
    print(b.delete_min())
    # print(b.get_attributes())
    assert b.get_attributes() == [[15, 'banana'],[35, 'orange'],[20, 'cherry'],[50, 'lime'],[45, 'lemon'],[40, 'kiwi'],[30, 'grape'],[80, 'pear'],[70, 'melon'],[60, 'mango'],[90, 'watermelon']]
    
    print('5 삽입 후')
    b.insert([5,'apple'])
    assert b.get_attributes() == [[5, 'apple'],[35, 'orange'],[15, 'banana'],[50, 'lime'],[45, 'lemon'],[20, 'cherry'],[30, 'grape'],[80, 'pear'],[70, 'melon'],[60, 'mango'],[90, 'watermelon'],[40, 'kiwi']]


    
test_core()