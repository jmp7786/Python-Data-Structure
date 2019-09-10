from sort.heap_sort.core import heap_sort, create_heap


def test_core():
    a = [-1, 54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
    create_heap(a)
    assert a == [-1, 93, 88, 77, 26, 77, 31, 49, 20, 17, 54, 11, 17, 22, 44, 17, 10]
    heap_sort(a)
    assert a == [-1, 10, 11, 17, 17, 17, 20, 22, 26, 31, 44, 49, 54, 77, 77, 88, 93]
