class Node:
    def __init__(self, k, v, left=None, right=None):
        self.key = k
        self.value = v
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def put(self, k, v):
        self.root = self._put(self.root, k, v)
    
    def _put(self, n, k, v):
        if n == None:
            return Node(k, v)
        if n.key > k:
            n.left = self._put(n.left, k, v)
        elif n.key < k:
            n.right = self._put(n.right, k, v)
        else:
            n.value = v
        
        return n
    
    def get(self, k):
        return self._get(self.root, k)
    
    def _get(self, n, k):
        if n == None:
            return None
        elif n.key > k:
            return self._get(n.left, k)
        elif n.key < k:
            return self._get(n.right, k)
        else:
            return n.value
    
    def get_min(self):
        return self._get_min(self.root)
    
    def _get_min(self, n):
        if n.left == None:
            return n
        
        return self._get_min(n.left)
    
    def delete_min(self):
        if self.root == None:
            raise Exception('트리가 비었습니다.')
        
        self.root = self._delete_min(self.root)
    
    def _delete_min(self, n):
        if n.left == None:
            return n.right
        
        n.left = self._delete_min(n.left)
        
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
            if n.left == None:
                return n.right
            if n.right == None:
                return n.left
            target = n
            n = self._get_min(target.right)
            n.right = self._delete_min(target.right)
            n.left = target.left
        
        return n
    
    def inorder(self, n):
        results = list()
        
        if n != None:
            if n.left:
                results.extend(self.inorder(n.left))
            
            results.append(n.key)
            
            if n.right:
                results.extend(self.inorder(n.right))
        
        return results