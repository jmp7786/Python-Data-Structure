class BFS:
    def __init__(self, a):
        self.N = len(a)
        self.a = a
        self.visited = [False] * self.N
    
    def bfs(self, i):
        results = list()
        
        queue = list()
        self.visited[i] = True
        queue.append(i)
        
        while len(queue) != 0:
            v = queue.pop(0)
            results.append(v)
            
            
            for w in self.a[v]:
                if not self.visited[w]:
                    self.visited[w] = True
                    queue.append(w)
        
        return results
    
    def get_attributes(self):
        results = list()
        for i in range(self.N):
            if not self.visited[i]:
                results += self.bfs(i)
        
        return results