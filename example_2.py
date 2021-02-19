# -*- coding: utf-8 -*-

import logging


class Node:
    def __init__(self, num: int):
        self.num = num
        self.next = None

    def __repr__(self):
        return f'<Node:{self.num}>'


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
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

    def get_length(self):
        return self.length

    def count_length(self, cnt=1):
        self.length += cnt

    def append(self, num):
        """ LinkedList 뒤에 Node 를 삽입 """
        if self.head is None:   # 1. LinkedList 에 아무 값도 없는 경우
            self.head = Node(num)   # -> self.head 에 Node 를 부착
            self.tail = self.head
        else:   # 2. LinkedList 에 하나의 값이라도 있는 경우
            self.tail.next = Node(num)  # -> LinkedList 의 맨 뒤의 Node 의 self.next 에 부착
            self.tail = self.tail.next
        self.count_length()

    def get_index_of_num(self, num):
        """ num 값을 가진 Node 객체의 index 를 찾아서 return """
        node = self.head
        idx = 0
        while node:    # while node is not None:
            if node.num == num:
                return idx
            node = node.next
            idx += 1
        raise CanNotFindNodeByValue(num)

    def find_node_at(self, idx):
        """ idx 자리에 있는 Node 객체를 찾아서 return """
        node = self.head
        index = 0
        while node:
            if index == idx:
                return node     # object:<Node:n>
            node = node.next
            index += 1
        raise CanNotFindNodeByIndex(idx)

    def insert_num_at_index(self, idx, num):
        """
        1. find_node_at()
        2. 그 자리에 num 을 넣는다.
        """
        node = Node(num)
        if idx == 0:    # 맨 첫 자리에 insert
            node.next = self.head
            self.head = node
        elif idx == self.get_length():    # 맨 끝 자리에 insert
            self.tail.next = node
        else:   # 중간 어딘가에 insert
            pre_node = self.find_node_at(idx-1)
            node.next = pre_node.next
            pre_node.next = node
        self.count_length()

    def delete_num_at_index(self, idx):
        """
        1. find_node_at()
        2. 그 자리에 num 을 지운다.
        """
        self.count_length(-1)


class CanNotFindNodeByValue(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'[CanNotFindNodeByValue] <Node:{str(self.num)}> not exist!'


class CanNotFindNodeByIndex(Exception):
    def __init__(self, idx):
        self.idx = idx

    def __str__(self):
        return f'[CanNotFindNodeByIndex] <Node> not exist at index {self.idx}!'


def main():
    lst = SinglyLinkedList()
    lst.append(5)
    lst.append(7)
    lst.append(12)
    lst.append(715)
    lst.append(14562)
    print(lst, end='\n')

    lst.insert_num_at_index(2, 19)
    print(lst, end='\n')

    lst.insert_num_at_index(0, 27)
    print(lst, end='\n')

    max_length = lst.get_length()
    lst.insert_num_at_index(max_length, 27)
    print(lst, end='\n')

    # Catch exception CanNotFindNodeByValue
    # ================================================
    # try:
    #     print(linked_list.get_index_of_num(9999))
    # except CanNotFindNodeByValue as error:
    #     logging.error(error)
    # ================================================

    # Catch exception CanNotFindNodeByIndex
    # ================================================
    # try:
    #     print(linked_list.find_node_at(9999))
    # except CanNotFindNodeByIndex as error:
    #     print(error)
    # ================================================


if __name__ == '__main__':
    main()
