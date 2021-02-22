# -*- coding: utf-8 -*-

import logging

class Node:
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'<Node:{self.num}>'


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        nodes = []
        now_node = self.head
        nodes.append(now_node)
        while now_node is not now_node.next \
                and now_node is not self.tail:
            now_node = now_node.next
            nodes.append(now_node)
        return str([node for node in nodes])

    def get_length(self):
        return self.length

    def append(self, num):  # 양방향 노드 추가
        node = Node(num)
        if self.head is None:   # DoublyLinkedList 에 노드가 하나도 없을 경우
            self.head = node
            self.tail = self.head
        else:   # DoublyLinkedList 에 노드가 하나라도 있을 경우
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
        self.length =+ 1


    def find_node_at_idx(self, idx):    # 원하는 자리의 노드 탐색
        node = self.head
        index = 0
        while node:
            if index == idx:
                return node
            node = node.next
            index += 1
        raise NotImplementedError



    def insert_node_at(self, idx, num):
        node = Node(num)
        target_node = self.find_node_at_idx(idx)
        if idx == 0:    # 연결리스트의 맨 앞에 노드를 삽입할 경우
            node = target_node
            target_node.prev = node
            node = self.head
            self.head.next = node.prev
        elif target_node == self.tail:  # 연결리스트의 맨 끝에 노드를 삽일할 경우
            self.tail.next = node
            node.prev = self.tail
            self.tail.next = self.tail
        else:   # 가운데 어딘가 노드를 삽입할 경우
            node = target_node
            before_data = target_node.prev
            target_node.prev = node
            node.prev = before_data
            before_data.next = node
        self.length += 1






    def delete_node_at(self):
        pass



#class CanNotFindNodeByIndex(Exception):
#    def __init__(self, idx):
#        self.idx = id
#    def __str__(self):
#        return f'[CanNotFindNodeByIndex] <Node> not exist at index {self.idx}!


def main():
    lst = DoublyLinkedList()

    lst.append(0)
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(lst)

    lst.insert_node_at(0, 1)
    print(lst)

    lst.insert_node_at(1, 2)
    print(lst)

if __name__ == '__main__':
    main()