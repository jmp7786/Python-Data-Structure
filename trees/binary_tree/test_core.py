from trees.binary_tree.core2 import BinaryTree, Node

def test_core():
    t = BinaryTree()
    
    n1 = Node(100)
    n2 = Node(200)
    n3 = Node(300)
    n4 = Node(400)
    n5 = Node(500)
    n6 = Node(600)
    n7 = Node(700)
    n8 = Node(800)
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    t.root = n1
    
    assert t.height(t.root) == 4
    assert t.preorder(t.root) == [100, 200, 400, 800, 500, 300, 600, 700]
    assert t.inorder(t.root) == [800, 400, 200, 500, 100, 600, 300, 700]
    assert t.postorder(t.root) == [800, 400, 500, 200, 600, 700, 300, 100]
    assert t.levelorder(t.root) == [100, 200, 300, 400, 500, 600, 700, 800]
    
    


test_core()
