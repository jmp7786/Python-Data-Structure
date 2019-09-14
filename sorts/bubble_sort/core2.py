def bubble_sort(li):
    length = len(li) - 1
    for i in range(length):
        for j in range(length - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
