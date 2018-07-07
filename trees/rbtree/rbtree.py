#!/home/francisco/Projects/Pycharm/pyalgorithms/venv/bin/python3
# -*- coding: utf-8 -*-


class RBNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 0


class RBTree:
    def __init__(self):
        self.root = None
        self.leaf = RBNode(None)
        self.leaf.color = 1

    def insert(self, value):
        node = RBNode(value)
        node.left = self.leaf
        node.right = self.leaf

        if not self.root:
            self.root = node
            self.root.color = 1
        else:
            current = self.root
            parent = current
            while current:
                if current == self.leaf:
                    break
                parent = current
                if node.value < current.value:
                    current = current.left
                else:
                    current = current.right

            node.parent = parent

            if node.value < parent.value:
                parent.left = node
            else:
                parent.right = node

        # self.fix_insert(node)

    def fix_insert(self, node):
        if node.parent:
            while node.parent.color == 0:
                if node.parent == node.parent.parent.left:
                    y = node.parent.parent.right
                    if y.color == 0:
                        node.parent.color = 1
                        y.color = 1
                        node.parent.parent.color = 0
                        node = node.parent.parent.parent
                    else:
                        if node == node.parent.right:
                            node = node.parent
                            print('left rotate left:', node)
                            self.rotate_left(node)
                        node.parent.color = 1
                        node.parent.parent.color = 0
                        print('left rotate right:', node.parent.value)
                        self.rotate_right(node.parent.parent)
                else:
                    if node.parent == node.parent.parent.right:
                        y = node.parent.parent.left
                        if y.color == 0:
                            node.parent.color = 1
                            y.color = 1
                            node.parent.parent.color = 0
                            node = node.parent.parent.parent
                        else:
                            if node == node.parent.left:
                                node = node.parent
                                print('right rotate right:', node.value)
                                self.rotate_right(node)
                            node.parent.color = 1
                            node.parent.parent.color = 0
                            print('right rotate left:', node.parent.value)
                            self.rotate_left(node.parent.parent)

                self.root.color = 1

    def rotate_left(self, x):
        y = x.right                 # define y
        x.right = y.left            # x right now igual y left
        y.left.parent = x           # y left now is x left
        y.parent = x.parent         # y parent is x parent

        if x == self.root:          # if x is root now y is root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y       # if x is the left child, then y is the left child
        else:
            x.parent.right = y      # if x is the right child, then y is the right child

        y.left = x                  # y left now is x
        x.parent = y                # x parent now is y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right.parent = x
        y.parent = x.parent

        if x == self.root:          # if x is root now y is root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y       # if x is the left child, then y is the left child
        else:
            x.parent.right = y      # if x is the right child, then y is the right child

        y.right = x
        x.parent = y

    def walk(self, node=None, flag=True):
        if not node and flag:
            node = self.root
        if node:
            flag = False
            if node == self.leaf:
                return
            self.walk(node.left, flag)
            if node.parent:
                print('{0}\t{1}\t{2}\t{3}\t{4}'.format(node.value, node.parent.value, node.left.value,
                                                      node.right.value, node.color))
            else:
                print('{0}\t{1}\t{2}\t{3}\t{4}'.format(node.value, None, node.left.value, node.right.value, node.color))
            self.walk(node.right, flag)

    def search(self, value):
        current = self.root
        while current and value != current.value:
            if current.value > value:
                current = current.left
            else:
                current = current.right

        return current

    def minimum(self, node=None):
        if not node:
            node = self.root

        while node.left != self.leaf:
            node = node.left

        return node

    def maximum(self, node=None):
        if not node:
            node = self.root

        while node.right != self.leaf:
            node = node.right

        return node

    def successor(self, value):
        current = self.search(value)

        if current.right != self.leaf:
            node = self.minimum(current.right)
            return node

        node = current.parent
        while current == node.right:
            current = node
            node = current.parent

        return node

    def delete(self, value):
        node = self.search(value)

        if node.left == self.leaf and node.right == self.leaf:
            if node.parent.left == node:
                node.parent.left = self.leaf
            else:
                node.parent.right = self.leaf
            del node
        elif (node.left == self.leaf) ^ (node.right == self.leaf):
            if node.parent.left == node:
                if node.right == self.leaf:
                    node.parent.left = node.left
                else:
                    node.parent.left = node.right
            else:
                if node.right == self.leaf:
                    node.parent.right = node.left
                else:
                    node.parent.right = node.right

            node.left.parent = node.parent
            node.right.parent = node.parent

            del node
        else:
            aux = self.successor(node.value)
            if node.parent.left == node:
                node.parent.left = aux
            else:
                node.parent.right = aux

            if aux.parent.left == aux:
                aux.parent.left = self.leaf
            else:
                aux.parent.right = self.leaf

            node.left.parent = aux
            node.right.parent = aux

            aux.left = node.left
            aux.right = node.right

            del node


if __name__ == '__main__':
    bt = RBTree()
    bt.insert(11)
    bt.insert(2)
    bt.insert(14)
    bt.insert(1)
    bt.insert(7)
    bt.insert(15)
    bt.insert(5)
    bt.insert(8)
    bt.insert(4)
    # bt.insert(3)
    print('node\tparent\tleft\tright\tcolor')
    print('***********************************')
    bt.walk()