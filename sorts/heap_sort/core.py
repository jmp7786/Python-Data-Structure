def downheap(a, i, hsize):
    while i * 2 <= hsize:
        k = i * 2
        if k < hsize and a[k] < a[k+1]:
            k += 1
        if a[i] > a[k]:
            break
            
        a[i], a[k] = a[k], a[i]
        
        i = k

def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2 +1)):
        downheap(a, i, hsize)
    
def heap_sort(a):
    hsize = len(a) - 1
    for i in range(hsize):
        a[1], a[hsize] = a[hsize], a[1]
        downheap(a, 1, hsize-1)
        hsize -= 1