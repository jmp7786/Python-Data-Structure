class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)

    def put_item(self,n, k, v):
        if n == None:
            return Node(k, v)
        if n.key > k:
            n.left = self.put_item(n.left, k, v)
        elif n.key < k:
            n.right = self.put_item(n.right, k ,v)
        else:
            n.value = v
            
        return n
    
    def get(self, k):
        return self.get_item(self.root, k)

    def get_item(self, n, k):
        if n == None :
            return None
        elif n.key > k:
            return self.get_item(n.left, k)
        elif n.key < k:
            return self.get_item(n.right, k)
        else:
            return n.value
        
    def get_min(self):
        if self.root == None:
            return None
        
        return self.minimum(self.root)
    
    def minimum(self, n):
        if n.left == None:
            return n
        
        return self.minimum(n.left)
    
    def delete_min(self):
        if self.root == None:
            raise Exception('트리가 비어있음')
        self.root = self.del_min(self.root)
    
    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n
    
    def delete(self, k):
        self.root = self._delete(self.root, k)
    
    def _delete(self, n, k):
        if n == None:
            return None
        
        if n.key > k:
            n.left = self._delete(n.left, k)
        elif n.key < k:
            n.right = self._delete(n.right, k)
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
            
        return n

    def inorder(self, n):
        results = list()
    
        if n != None:
            if n.left:
                results += self.inorder(n.left)
        
            results.append(n.key)
        
            if n.right:
                results += self.inorder(n.right)
    
        return results

