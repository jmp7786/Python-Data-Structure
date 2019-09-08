from trees.binary_heap.core import BinaryHeap

def test_core():
    a = [None] * 1
    a.append([50, 'lime'])
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([20, 'cherry'])
    a.append([60, 'mango'])
    a.append([35, 'orange'])
    a.append([30, 'grape'])
    a.append([15, 'banana'])
    a.append([10, 'apricot'])
    a.append([45, 'lemon'])
    a.append([40, 'kiwi'])
    
    
    b = BinaryHeap(a)
    print('힙 만들기 전')
    b.print_heap()
    b.create_heap()
    print('최소힙')
    
    b.print_heap()
    
    print('최솟값 삭제 후')
    print(b.delete_min())
    b.print_heap()
    print('5 삽입 후')
    b.insert([5,'apple'])
    b.print_heap()
    
test_core()