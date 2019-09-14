def selection_sort(a):
    for i in range(len(a)-1):
        _min = i
        for j in range(i, len(a)):
            if a[_min] > a[j]:
                _min = j
        a[i], a[_min] = a[_min], a[i]
