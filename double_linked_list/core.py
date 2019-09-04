class DList:
    class Node:
        def __init__(self, item, prev, link):  # 노드 생성자
            self.item = item  # 항목
            self.prev = prev  # 뒤 노드 레퍼런스
            self.next = link  # 앞 노드 레퍼런스

    def __init__(self):  # 이중 연결 리스트 생성자
        # 두 더미 노드(dummy node)를 생성하는데 항목을 저장하지는 않음
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    def size(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def insert_before(self, p, item):  # 새 노드를 노드 p 앞에 삽입
        t = p.prev
        n = self.Node(item, t, p)  # 생성한 노드를 n이 참조
        p.prev = n  # 뒤 노드와 새 노드 연결
        t.next = n  # 앞 노드와 새 노드 연결
        self.size += 1

    def insert_after(self, p, item):  # 새 노드를 노드 p 뒤에 삽입
        t = p.next
        n = self.Node(item, p, t)  # 생성한 노드를 n이 참조
        t.prev = n  # 앞 노드와 새 노드 연결
        p.next = n  # 뒤 노드와 새 노드 연결
        self.size += 1
        
    def delete(self, x):  # 노드 x 삭제
        # x가 참조하는 노드는 연결 리스트에서 분리되어 가비지 컬렉션에 의해 처리됨
        f = x.prev
        r = x.next
        f.next = r  # x를 건너뛰고 x의 앞뒤 노드를 연결
        r.prev = f  # x를 건너뛰고 x의 앞뒤 노드를 연결
        self.size -= 1
        return x.item

    def print_list(self):
        if self.isempty():
            print('List is empty.')
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next  # 노드를 차례로 방문



#
# 왜 dummy data를 넣는 것이지???
# insert front 를 넣어도 되잖아
