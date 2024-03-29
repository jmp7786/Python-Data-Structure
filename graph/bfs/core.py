class BFS:
    def __init__(self, tree):
        self.tree = tree
        self.size = len(tree)
        self.visitied = [False] * self.size
    
    def bfs(self, i):
        queue = list()
        results = list()
        
        queue.append(i)
        self.visitied[i] = True
        
        while len(queue) != 0:
            value = queue.pop(0)
            results.append(value)
            
            for j in self.tree[value]:
                if not self.visitied[j]:
                    self.visitied[j] = True
                    queue.append(j)
        
        return results
    
    def get_attributes(self):
        results = list()
        
        for i in range(self.size):
            if not self.visitied[i]:
                results += self.bfs(i)
                
        return results
        