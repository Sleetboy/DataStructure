# 데이터와 포인터로 구성된 노드 클래스를 만든다.
# -*- coding: utf-8 -*-

import logging

class Node:
    def __init__(self, num: int):
        self.num = num
        self.next = None

    def __repr__(self):
        return f'<Node:{self.num}>'

# head 와 length를 가지는 연결 리스트를 만든다.
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        nodes = []
        now_node = self.head
        while True:
            if now_node is None:
                break
            nodes.append(now_node)
            now_node = now_node.next
        return str([node for node in nodes])

# 노드 탐색
    def search_node(self, idx):
        target_node = self.head
        count = 0
        while target_node is not None:
            if count == idx:
                return target_node
            target_node = target_node.next
            count += 1
        raise NotImplementedError


# 노드를 더하는 기능
    def append(self, num):
        if self.head is None:   #노드가 하나도 없을 경우
            self.head = Node(num)
            self.tail = self.head
        else:   #노드가 하나라도 있을 경우
            self.tail.next = Node(num)
            self.tail = self.tail.next
        self.length += 1

# 원하는 인덱스에 노드 삽입
    def insert_node(self, idx, num):
        node = Node(num)
        if idx == 0:    # 0번째 인덱스에 삽입
            node.next = self.head
            self.head = node
            self.length += 1
        elif 0 < idx < self.length - 1:  # 중간 어딘가 인덱스에 삽입
            pre_node = self.search_node(idx-1)
            node.next = pre_node.next
            pre_node.next = node
            self.length += 1
        elif idx == self.length: # 마지막 인덱스에 삽입
            self.tail.next = node
            self.tail = self.tail.next
            self.length += 1
        else:
            raise NotImplementedError


# 원하는 인덱스의 노드 삭제
    def delete_node(self, idx):
        if self.search_node(idx) is not None:
            if idx == 0:    # 0번째 노드 삭제
                self.head = self.search_node(idx).next
                self.length += -1
            elif 0 < idx < self.length - 1:     # 중간 어딘가의 노드 삭제
                pre_node = self.search_node(idx-1)
                pre_node.next = self.search_node(idx).next
                self.length += -1
            elif idx == self.length:    # 마지막 노드 삭제
                pre_node = self.search_node(idx-1)
                pre_node.next = None
                self.tail = pre_node
                self.length += -1
            else:
                raise NotImplementedError
        else:   # 노드가 하나도 없을 경우
            raise NotImplementedError

def main():
    lst = LinkedList()

    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    print(lst)

    lst.insert_node(0, 0)
    print(lst)

    lst.insert_node(2, 10)
    print(lst)

    print(lst.length)


    max_length = lst.length
    lst.insert_node(max_length, 100)
    print(lst)
    print(lst.head)

    lst.delete_node(0)
    print(lst)

    lst.delete_node(3)
    print(lst)

    print(max_length)

    lst.delete_node(max_length)
    print(lst)

if __name__ == '__main__':
    main()
