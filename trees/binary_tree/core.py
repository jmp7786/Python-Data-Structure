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
                results.extend(self.preorder(n.left))
            if n.right:
                results.extend(self.preorder(n.right))
        
        return results
    
    def inorder(self, n):
        results = list()
        
        if n != None:
            if n.left:
                results.extend(self.inorder(n.left))
            
            results.append(n.item)
            
            if n.right:
                results.extend(self.inorder(n.right))
            
        return results

    def postorder(self, n):
        results = list()
        
        if n != None:
            if n.left:
                results.extend(self.postorder(n.left))
            if n.right:
                results.extend(self.postorder(n.right))
            
            results.append(n.item)
        
        return results

    def levelorder(self, n):
        results = list()
        q = list()
        
        q.append(n)
    
        while len(q) != 0:
            v = q.pop(0)
            results.append(v.item)
            
            if v.left:
                q.append(v.left)
            if v.right:
                q.append(v.right)
        
        return results

    def height(self, n):
        if n == None:
            return 0
        
        return max(self.height(n.left), self.height(n.right)) + 1