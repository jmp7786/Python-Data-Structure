class BinaryHeap:
    def __init__(self, a):
        self.list = a
        self.size = len(a) - 1
    
    def create_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.downheap(i)
    
    def insert(self, key_value):
        self.size += 1
        self.list.append(key_value)
        self.upheap(self.size)
    
    def delete_min(self):
        if self.size == 0:
            return None
        
        minimum = self.list[1]
        self.list[1], self.list[-1] = self.list[-1], self.list[1]
        del self.list[-1]
        self.size -= 1
        self.downheap(1)
        
        return minimum
    
    def downheap(self, i):
        print(i,1)
        while 2 * i <= self.size:
            print(i, 2)
            k = 2 * i # 자식의 위치
            # 자식의 위기가 전체 사이즈보다 작고, 첫번째 자식이 두번째 자식보다 크면 k를 하나 올린다.(두번째 자식을 선택)
            if k < self.size and self.list[k][0] > self.list[k + 1][0]:
                k += 1
            # 만약 부모의 우선 순위가 자식의 우선순위보다 작다면 그만
            if self.list[i][0] < self.list[k][0]:
                break
            # 자신과 자식의 위치를 교환해준다.
            self.list[i], self.list[k] = self.list[k], self.list[i]
            # 부모와 자식간에 위치를 바꿔주고 바꾼 자손의 자손이 변경사항을 적용해야 하는지 다시 루프를 돌린다.
            i = k
            
    
    def upheap(self, j):
        # 인덱스가 0 은 아닌지 체크, 부모의 값이 자신의 값보다 크다면 위치 변경, 자신의 위치를 부모와 변경하면서 계속 진행
        while j > 1 and self.list[j // 2][0] > self.list[j][0]:
            self.list[j], self.list[j // 2] = self.list[j // 2], self.list[j]
            j = j // 2
    
    def print_heap(self):
        for i in range(1, self.size + 1):
            print('[%2d' % self.list[i][0], self.list[i][1], ']', end='')
        print('\n힙 크기 = ', self.size)



