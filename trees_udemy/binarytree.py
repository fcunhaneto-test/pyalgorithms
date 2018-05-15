#!/home/francisco/.pyvenv/mypython3/bin/python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, node):
        if not self.root:
            self.root = Node(value)
            return
        else:
            node = Node(value)
            current = self.root

    def walk(self, node=None, flag=True):
        if not node and flag:
            node = self.root
        if node:
            flag = False
            self.walk(node.left, flag)
            print(node.value)
            self.walk(node.right, flag)


if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(11)
    bt.insert(2)
    bt.insert(14)
    bt.insert(1)
    bt.insert(7)
    bt.insert(15)
    bt.insert(5)
    bt.insert(8)
    bt.walk()