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

    def __len__(self):
        return self.length

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
                self.length -= 1
            elif 0 < idx < self.length - 1:     # 중간 어딘가의 노드 삭제
                pre_node = self.search_node(idx-1)
                pre_node.next = self.search_node(idx).next
                self.length -= 1
            elif idx == self.length:    # 마지막 노드 삭제
                pre_node = self.search_node(idx-1)
                pre_node.next = None
                self.tail = pre_node
                self.length -= 1
            else:
                raise NotImplementedError
        else:   # 노드가 하나도 없을 경우
            raise NotImplementedError

    def get_length(self):
        return self.length


def main():
    lst = LinkedList()

    print('================ append ================')
    lst.append(1)
    print(lst)
    lst.append(2)
    print(lst)
    lst.append(3)
    print(lst)
    lst.append(4)
    print(lst)
    lst.append(5)
    print(lst)

    print('================ insert ================')
    lst.insert_node(0, 0)
    print(lst)
    lst.insert_node(2, 10)
    print(lst)

    max_length = lst.length
    # 이 연산을 하는 순간, max_length 는 LinkedList 안의 item 개수가 변경되더라도 개수는 상관없이 무조건 7 개
    # -> deepcopy 로 int 값이 할당되기 때문
    # -> call by value, call by reference, passed by assignment 찾아보기

    lst.insert_node(max_length, 100)
    print(lst)

    print('================ length ================')
    # 직접 class 의 member variable(instance variable) 에 접근하여 값을 출력(변수명이 '_'으로 시작하면 private 이라 접근 불가)
    print(lst.length)

    # 직접 class 의 member variable(instance variable) 에 접근하여 값을 다른 변수에 할당하고, 그 값을 출력
    # 위의 line 119와 동일
    max_length = lst.length
    print(max_length)

    # list 의 length 를 return 하는 custom method 를 만들어서 사용
    print(lst.get_length())

    # python special method 를 활용하여 길이를 구함, 가장 Pythonic 한 방법
    print(len(lst))

    print('================ delete ================')

    lst.delete_node(0)
    print(lst)
    lst.delete_node(3)
    print(lst)
    lst.delete_node(max_length)
    print(lst)


if __name__ == '__main__':
    main()
