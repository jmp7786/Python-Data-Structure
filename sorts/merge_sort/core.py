def merge(a, b, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high+1):
        if i > mid:
            b[k] = a[j]
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1
        elif a[i] > a[j]:
            b[k] = a[j]
            j += 1
        else:
            b[k] = a[i]
            i += 1
    
    for k in range(low, high+1):
        a[k] = b[k]

def merge_sort(a, b, low, high):
    if low >= high:
        return
    
    mid = low + (high - low) // 2
    merge_sort(a, b, low, mid)
    merge_sort(a, b, mid+1, high)
    merge(a, b, low, mid, high)