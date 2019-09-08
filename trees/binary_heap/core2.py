class BinaryHeap:
    def __init__(self, a):
        self.list = a
        self.size = len(a) - 1
    
    def create_heap(self):
        for i in range(self.size, 0, -1):
            self.downheap(i)
    
    def downheap(self, i):
        while i * 2 <= self.size:
            k = i * 2
            if k < self.size and self.list[k][0] > self.list[k+1][0]:
                k += 1
            if self.list[i][0] < self.list[k][0]:
                break
            
            self.list[i], self.list[k] = self.list[k], self.list[i]
            
            i = k
    
    def upheap(self, j):
        while j > 1 and self.list[j//2][0] > self.list[j][0]:
            self.list[j], self.list[j//2] = self.list[j//2], self.list[j]
            j = j//2
            
    def delete_min(self):
        if self.size == 0:
            return None
        
        minimum = self.list[1]
        self.list[1], self.list[-1] = self.list[-1], self.list[1]
        del self.list[-1]
        self.size -= 1
        self.downheap(1)
    
    def insert(self, n):
        self.size += 1
        self.list.append(n)
        self.upheap(self.size)
    
    def get_attributes(self):
        return self.list[1:]
        