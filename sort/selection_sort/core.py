def selection_sort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i, len(a)):
            if a[min] > a[j]:
                min = j
        
        a[min], a[i] = a[i], a[min]
