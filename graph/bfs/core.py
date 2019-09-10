class BFS:
    def __init__(self, tree):
        self.tree = tree
        self.size = len(tree)
        self.visited = [False] * self.size
        
    def bfs(self, i):
        results = list()
        queue = list()
        
        self.visited[i] = True
        queue.append(i)
        
        while len(queue) != 0:
            value = queue.pop(0)
            results.append(value)
            
            for j in self.tree[value]:
                if not self.visited[j]:
                    self.visited[j] = True
                    queue.append(j)
        
        return results
        
    
    def get_attributes(self):
        results = list()
        
        for i in range(self.size):
            if not self.visited[i]:
                results += self.bfs(i)
                
        return results