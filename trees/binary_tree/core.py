class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree:
    root = None
    
    def preorder(self, n):
        result = list()
        
        if n != None:
            result.append(n.item)
            
            if n.left:
                result += self.preorder(n.left)
            
            if n.right:
                result += self.preorder(n.right)
        
        return result
    
    def inorder(self, n):
        result = list()
        
        if n != None:
            if n.left:
                result += self.inorder(n.left)
            
            result.append(n.item)
            
            if n.right:
                result += self.inorder(n.right)
        
        return result
    
    def postorder(self, n):
        result = list()
        
        if n != None:
            if n.left:
                result += self.postorder(n.left)
            
            if n.right:
                result += self.postorder(n.right)
            
            result.append(n.item)
        
        return result
    
    def levelorder(self, root):
        q = list()
        result = list()
        
        q.append(root)
        
        while len(q) != 0:
            t = q.pop(0)
            
            result.append(t.item)
            
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        
        return result
    
    def height(self, root):
        if root == None:
            return 0
        
        return max(self.height(root.left), self.height(root.right)) + 1
