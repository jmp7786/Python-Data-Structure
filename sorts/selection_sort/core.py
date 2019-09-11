def selection_sort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i, len(a)):
            if a[min] > a[j]:
                min = j
        
        a[min], a[i] = a[i], a[min]

def bubble_sort(li):
    length = len(li) - 1
    for i in range(length):
        for j in range(length-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

if __name__ == "__main__":
    li = [10,2,3,4,1,7,0]
    bubble_sort(li)
    print(li)
    