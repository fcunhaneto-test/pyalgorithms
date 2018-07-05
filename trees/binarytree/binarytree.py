#!/home/francisco/Projects/Pycharm/pyalgorithms/venv/bin/python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.leaf = Node(None)

    def insert(self, key):
        node = Node(key)
        node.left = self.leaf
        node.right = self.leaf

        if not self.root:
            self.root = node
        else:
            current = self.root
            parent = current
            while current != self.leaf:
                parent = current
                if node.key < current.key:
                    current = current.left
                elif node.key > current.key:
                    current = current.right
                else:
                    return False

            node.parent = parent

            if node.key < parent.key:
                parent.left = node
            else:
                parent.right = node

        return True

    def walk_in_order(self, node=None):
        if not node:
            node = self.root

        if node != self.leaf:

            self.walk_in_order(node.left)
            if node.parent:
                print('{0}\t{1}\t{2}\t{3}'.format(node.key, node.parent.key, node.left.key, node.right.key))
            else:
                print('{0}\t{1}\t{2}\t{3}'.format(node.key, None, node.left.key, node.right.key))
            self.walk_in_order(node.right)

    def walk_pos_order(self, node=None):
        if not node:
            node = self.root

        if node != self.leaf:

            self.walk_pos_order(node.right)
            if node.parent:
                print('{0}\t{1}\t{2}\t{3}'.format(node.key, node.parent.key, node.left.key, node.right.key))
            else:
                print('{0}\t{1}\t{2}\t{3}'.format(node.key, None, node.left.key, node.right.key))
            self.walk_pos_order(node.left)

    def search(self, value):
        current = self.root
        if value == current.key:
            return self.root

        while value != current.key and current != self.leaf:
            if current.key > value:
                current = current.left
            else:
                current = current.right

        if current == self.leaf:
            return False

        return current

    def minimum(self, node=None):
        if not node:
            node = self.root

        while node != self.leaf:
            mini = node
            node = node.left

        return mini

    def maximum(self, node=None):
        if not node:
            node = self.root

        while node != self.leaf:
            maxi = node
            node = node.right

        return maxi

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
        node = self.search(value)
        if not node:
            return False

        if node == self.root:
            self._remove_root(node)
        elif node.left == self.leaf and node.right == self.leaf:
            self._remove_if_leaf(node)
        elif (node.left == self.leaf) ^ (node.right == self.leaf):
            self._remove_if_one_child(node)
        else:
            self._remove_if_two_childs(node)

        del node

        return True

    def _remove_if_leaf(self, node):
        if node.parent.left == node:
            node.parent.left = self.leaf
        else:
            node.parent.right = self.leaf

    def _remove_if_one_child(self, node):
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

    def _remove_if_two_childs(self, node):
        successor = self.successor(node.key)

        if successor == node.right:
            if node == node.parent.left:
                node.parent.left = successor
            else:
                node.parent.right = successor

            successor.parent = node.parent
            successor.left = node.left
            successor.left.parent = successor
        else:
            if node == node.parent.left:
                node.parent.left = successor
            else:
                node.parent.right = successor

            successor.parent.left = successor.right
            successor.left = node.left
            successor.right = node.right

            node.right.parent = successor
            node.left.parent = successor
            successor.parent = node.parent

    def _remove_root(self, node):
        if node.left == self.leaf and node.right == self.leaf:
            self.root = None
        elif (node.left == self.leaf) ^ (node.right == self.leaf):
            if node.left != self.leaf:
                self.root = node.left
            else:
                self.root = node.right

            self.root.parent = None
        else:
            successor = self.successor(node.key)
            if successor == node.right:

                successor.parent = None
                successor.left = self.root.left
                self.root.left.parent = successor
                self.root = successor
            else:
                if successor.right:
                    successor.right.parent = successor.parent

                successor.parent.left = successor.right
                successor.left = node.left
                successor.right = node.right

                node.left.parent = successor
                node.right.parent = successor
                successor.parent = None
                self.root = successor


if __name__ == '__main__':
    # from trees import handletrees
    # handletrees.handle_trees()
    bt = BinaryTree()
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    bt.insert(50)
    bt.insert(25)
    bt.insert(15)
    bt.insert(30)
    bt.insert(10)
    bt.insert(14)
    bt.insert(29)
    bt.insert(40)
    # # bt.insert(80)
    # # bt.insert(75)
    # # bt.insert(80)
    # # bt.insert(60)
    # # bt.insert(74)
    # # bt.insert(73)
    # # bt.insert(90)
    # # bt.insert(58)
    # bt.walk_in_order()
    # print('***********************************************')
    # bt.remove(50)
    bt.walk_in_order()
    # print('***********************************************')
