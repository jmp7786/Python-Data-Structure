from sorts.bubble_sort.core import bubble_sort

def test_core():
    li = [10, 2, 3, 4, 1, 7, 0]
    bubble_sort(li)
    assert li == [0, 1, 2, 3, 4, 7, 10]
