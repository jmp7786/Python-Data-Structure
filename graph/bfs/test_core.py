from graph.bfs.core import BFS


def test_core():
    tree = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]

    assert BFS(tree).get_attributes() == [0, 2, 1, 3, 9, 8, 4, 5, 7, 6]

# 피보나치 수열 재귀, for?
# 팩토리얼 재귀, for
# 버블정렬
# 싱글톤 구현
