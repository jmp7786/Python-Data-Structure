from search_tree.binary_search_tree.core import BinarySearchTree

def test_core():
    t = BinarySearchTree()
    
    t.put(500, 'apple')
    t.put(600, 'banana')
    t.put(200, 'melon')
    t.put(100, 'orange')
    t.put(400, 'lime')
    t.put(250, 'kiwi')
    t.put(150, 'grape')
    t.put(800, 'peach')
    t.put(700, 'cherry')
    t.put(50, 'pear')
    t.put(350, 'lemon')
    t.put(10, 'plum')
    
    assert t.inorder(t.root) == [10, 50, 100, 150, 200, 250, 350, 400, 500, 600, 700, 800]
    
    assert t.get(250) == 'kiwi'
    
    t.delete(200)
    assert t.inorder(t.root) == [10, 50, 100, 150, 250, 350, 400, 500, 600,
        700, 800]
    
    
    assert t.get_min().key == 10

    t.delete_min()
    
    assert t.get_min().key == 50
    assert t.inorder(t.root) == [50, 100, 150, 250, 350, 400, 500, 600,
        700, 800]

    

test_core()