class DFS:
    def __init__(self, tree):
        self.size = len(tree)
        self.tree = tree
        self.visitied = [False] * self.size
    
    def dfs(self, i):
        results = list()
        
        results.append(i)
        self.visitied[i] = True
        
        for j in self.tree[i]:
            if not self.visitied[j]:
                results += self.dfs(j)
        
        return results
    
    def get_attributes(self):
        results = list()
        
        for i in range(self.size):
            if not self.visitied[i]:
                results += self.dfs(i)
        
        return results
        