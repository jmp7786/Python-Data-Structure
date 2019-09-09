class DFS:
    def __init__(self, a):
        self.N = len(a)
        self.a = a
        self.visited = [False] * self.N

    def dfs(self, v):
        results = list()
        
        self.visited[v] = True
        results.append(v)
        for w in self.a[v]:
            if not self.visited[w]:
                results += self.dfs(w)
                
        return results


    def get_attribute(self):
        results = list()
        
        for i in range(self.N):
            if not self.visited[i]:
                results += self.dfs(i)
                
        return results
