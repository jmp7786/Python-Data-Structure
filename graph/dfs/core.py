class DFS:
    def __init__(self, tree):
        self.size = len(tree)
        self.tree = tree
        self.visited = [False] * self.size
    
    def dfs(self, i):
        results = list()
        self.visited[i] = True
        
        results.append(i)
        
        for j in self.tree[i]:
            if not self.visited[j]:
                results += self.dfs(j)
                
        return results
    
    def get_attributes(self):
        results = list()
        
        for i in range(self.size):
            if not self.visited[i]:
                results += self.dfs(i)
                
        return results

    