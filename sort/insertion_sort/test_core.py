from sort.insertion_sort.core import insertion_sort


def test_core():
    a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
    insertion_sort(a)
    
    assert a == [10, 11, 17, 17, 17, 20, 22, 26, 31, 44, 49, 54, 77, 77, 88, 93]

