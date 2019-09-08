from hash.closed_hash.core import Chaining

def test_core():
    t = Chaining(13)
    
    t.put(25,'grape')
    t.put(37,'apple')
    t.put(18,'banana')
    t.put(55,'cherry')
    t.put(22,'mango')
    t.put(35,'lime')
    t.put(50,'orange')
    t.put(63,'watermelon')
    
    assert t.get(50) == 'orange'
    assert t.get(63) == 'watermelon'
    assert t.get(37) == 'apple'
    assert t.get(37) == 'apple'
    
    assert t.get_attributes() == [[], [], [], [[55, 'cherry']], [], [[18, 'banana']], [], [], [], [[35, 'lime'], [22, 'mango']], [], [[63, 'watermelon'], [50, 'orange'], [37, 'apple']], [[25, 'grape']]]
    



