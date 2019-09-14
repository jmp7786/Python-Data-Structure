class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
        
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preorder(self, n):
        results = list()
        
        if n != None:
            results.append(n.item)
            
            if n.left:
                results += self.preorder(n.left)
            
            if n.right:
                results += self.preorder(n.right)
            
        return results

    def inorder(self, n):
        results = list()
        
        if n != None:
            if n.left:
                results += self.inorder(n.left)
            
            results.append(n.item)
            
            if n.right:
                results += self.inorder(n.right)
            
        return results

    def postorder(self, n):
        results = list()
        
        if n != None:
            if n.left:
                results += self.postorder(n.left)
            if n.right:
                results += self.postorder(n.right)
            
            results.append(n.item)
    
        return results

    def levelorder(self, root):
        results = list()
        q = list()
        
        q.append(root)
        
        while len(q) != 0:
            t = q.pop(0)
            
            results.append(t.item)
            
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            
        
        return results
    
    def height(self, n):
        if n == None:
            return 0
        
        return max(self.height(n.left), self.height(n.right) ) + 1
        
        
        