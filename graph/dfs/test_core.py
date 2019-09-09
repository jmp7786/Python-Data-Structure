from graph.dfs.core import DFS


def test_core():
    a = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5],
        [3], [3]]
    
    assert DFS(a).get_attribute() == [0, 2, 3, 9, 8, 1, 4, 5, 7, 6]
    
