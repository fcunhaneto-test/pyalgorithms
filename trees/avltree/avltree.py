#!/home/francisco/Projects/Pycharm/pyalgorithms/venv/bin/python3
# -*- coding: utf-8 -*-


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height_left = 0
        self.height_right = 0


class AVLTree:
    def __init__(self):
        self.root = None
        self.leaf = AVLNode(None)
        self.leaf.height = -1

    def insert(self, key):
        node = AVLNode(key)
        node.left = self.leaf
        node.right = self.leaf
        node.height = 0

        if not self.root:
            self.root = node
        else:
            current = self.root
            parent = current

            while current:
                if current == self.leaf:
                    break

                parent = current
                if node.key < current.key:
                    current = current.left
                elif node.key > current.key:
                    current = current.right
                elif node.key == current.key:
                    return False

            node.parent = parent

            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node

            self.calculate_height(node)
            self.fix_violation(node)

        return True

    def calculate_height(self, node):
        current = node

        while current:
            current.height = max(current.left.height, current.right.height) + 1
            current = current.parent

    def fix_violation(self, node):
        previous = node
        current = node.parent
        fb1, fb2 = 0, 0
        while current:
            # print('current:', current.key, 'previous:', previous.key, )
            fb1 = current.left.height - current.right.height
            fb2 = previous.left.height - previous.right.height
            # print('fb', fb1, fb2)
            if fb1 >= 2 and fb2 >= 0:
                self.rotate_right(current)
                current.height -= 2
                self.calculate_height(current)
                break
            if fb1 <= -2 and fb2 <= 0:
                self.rotate_left(current)
                current.height -= 2
                self.calculate_height(current)
                break
            if fb1 >= +2 and fb2 <= 0:
                self.rotate_left(previous)
                previous.height -= 2
                self.calculate_height(previous)
                self.rotate_right(current)
                current.height -= 2
                self.calculate_height(current)
                break
            if fb1 <= -2 and fb2 >= 0:
                self.rotate_right(previous)
                previous.height -= 2
                self.calculate_height(previous)
                self.rotate_left(current)
                current.height -= 2
                self.calculate_height(current)
                break
            previous = current
            current = current.parent

    def rotate_left(self, x):
        y = x.right  # define y
        x.right = y.left  # x right now igual y left
        y.left.parent = x  # y left now is x left
        y.parent = x.parent  # y parent is x parent

        if x == self.root:  # if x is root now y is root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y  # if x is the left child, then y is the left child
        else:
            x.parent.right = y  # if x is the right child, then y is the right child

        y.left = x  # y left now is x
        x.parent = y  # x parent now is y

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right.parent = x
        y.parent = x.parent

        if x == self.root:  # if x is root now y is root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y  # if x is the left child, then y is the left child
        else:
            x.parent.right = y  # if x is the right child, then y is the right child

        y.right = x
        x.parent = y

    def walk_in_order(self, node=None):
        if not node:
            node = self.root

        if node != self.leaf:

            self.walk_in_order(node.left)

            fb = node.left.height - node.right.height
            if node.parent:

                print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(node.key, node.parent.key, node.left.key, node.right.key,
                                                       node.height, fb))
            else:
                print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(node.key, None, node.left.key, node.right.key,
                                                            node.height, fb))

            self.walk_in_order(node.right)

    def walk_pos_order(self, node=None):
        if not node:
            node = self.root

        if node != self.leaf:

            self.walk_pos_order(node.right)
            if node.parent:
                print('{0}\t{1}\t{2}\t{3}\t{4}'.format(node.key, node.parent.key, node.left.key, node.right.key,
                                                  node.height, ))
            else:
                print('{0}\t{1}\t{2}\t{3}\t{4}'.format(node.key, None, node.left.key, node.right.key, node.height))

            self.walk_pos_order(node.left)

    def search(self, value):
        current = self.root
        while current and value != current.key:
            if not current.key:
                return False

            if current.key > value:
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
        if not current:
            return False
        elif current.right != self.leaf:
            node = self.minimum(current.right)
            return node

        node = current.parent
        while node and current == node.right:
            current = node
            node = current.parent

        if not node:
            return self.maximum()

        return node

    def predecessor(self, value):
        current = self.search(value)
        if not current:
            return False
        elif current.left != self.leaf:
            node = self.maximum(current.left)
            return node

        node = current.parent
        while node and current == node.left:
            current = node
            node = current.parent

        if not node:
            return self.minimum()

        return node

    def remove(self, value):
        pass


if __name__ == '__main__':
    bt = AVLTree()
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    bt.insert(11)
    bt.insert(2)
    bt.insert(14)
    bt.insert(1)
    bt.insert(7)
    bt.insert(15)
    bt.insert(5)
    bt.insert(8)
    bt.walk_in_order()
    print('***********************************************')
    bt.insert(4)
    bt.walk_in_order()
    print('***********************************************')
    # bt.remove(12)
    # bt.walk_in_order()
    # print('***********************************************')

