class BinaryHeap:
    def __init__(self, a):
        self.a = a
        self.size = len(a) - 1
    
    def create_heap(self):
        for i in range(self.size//2, 0, -1):
            self.downheap(i)
    
    def downheap(self, i):
        while i * 2 <= self.size:
            k = i * 2
            if k < self.size and self.a[k][0] > self.a[k+1][0]:
                k += 1
            if self.a[i] < self.a[k]:
                break
            
            self.a[i], self.a[k] = self.a[k], self.a[i]
            
            i = k
    
    def upheap(self, i):
        while i > 1 and self.a[i//2][0] > self.a[i][0]:
            self.a[i], self.a[i//2] = self.a[i//2], self.a[i]
            i = i//2
    
    def insert(self, n):
        self.size += 1
        self.a.append(n)
        self.upheap(self.size)
    
    def delete_min(self):
        if self.size == 0:
            return
    
        _min = self.a[1]
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]
        self.size -= 1
        self.downheap(1)
        
        return _min
    
    def get_attributes(self):
        return self.a[1:]
    
        
        
        
        