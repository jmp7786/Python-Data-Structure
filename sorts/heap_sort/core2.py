def downheap(a, i, size):
    while 2 * i <= size:
        k = 2 * i
        if k < size and a[k] < a[k + 1]:
            k += 1
        if a[i] >= a[k]:
            break
        
        a[i], a[k] = a[k], a[i]
        i = k


def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize // +1)):
        downheap(a, i, hsize)


def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(a, 1, N - 1)
        N -= 1



