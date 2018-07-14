#!/home/francisco/Projects/Pycharm/pyalgorithms/venv/bin/python3
# -*- coding: utf-8 -*-

from trees.node import Node


class BinaryTree:
    def __init__(self):
        """
        Start the Binary Tree class.
        """
        self.root = None
        self.leaf = Node(None)

    def insert(self, key):
        """
        Insert key value in Binary Tree.
        :param key:
        :return:
        """
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
        """
        Traverses the sub-tree from the node given in ascending order and shows it on a table.
        :param node:
        :return:
        """
        if not node:
            node = self.root

        if node.key:

            self.walk_in_order(node.left)

            if node.parent:

                print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(node.key, node.parent.key, node.left.key, node.right.key,
                                                            node.height, node.color))
            else:
                print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(node.key, None, node.left.key, node.right.key, node.height,
                                                            node.color))

            self.walk_in_order(node.right)

    def walk_pos_order(self, node=None):
        """
        Traverses the subtree from the given node in descending order and shows it in a table.
        :param node:
        :return:
        """
        if not node:
            node = self.root

        if node.key:

            self.walk_pos_order(node.right)

            if node.parent:

                print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(node.key, node.parent.key, node.left.key, node.right.key,
                                                            node.height, node.color))
            else:
                print('{0}\t{1}\t{2}\t{3}\t{4}\t{5}'.format(node.key, None, node.left.key, node.right.key, node.height,
                                                            node.color))

            self.walk_pos_order(node.left)

    def search(self, value):
        """
        Find a node from the value of your key.
        :param value:
        :return:
        """
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
        """
        Find a minimum key value in the subtree, starting at a given node.
        :param node:
        :return:
        """
        if not node:
            node = self.root

        while node.left.key:
            node = node.left

        return node

    def maximum(self, node=None):
        """
        Find a maximum key value in the subtree, starting at a given node.
        :param node:
        :return:
        """
        if not node:
            node = self.root

        while node.right.key:
            node = node.right

        return node

    def successor(self, value):
        """
        Find the node successor in the tree from his given key value.
        :param value:
        :return:
        """
        current = self.search(value)
        if not current:
            return False
        elif current.right.key:
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
        """
        Find the node predecessor in the tree from his given key value.
        :param value:
        :return:
        """
        current = self.search(value)
        if not current:
            return False
        elif current.left.key:
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
        """
        Remove node where key is equal of given value.
        :param value: numeric
        """
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
        """
        Remove given node where node is a leaf.
        :param node:
        :return:
        """
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
        """
        Remove given node where if node have only one child.
        :param node:
        :return:
        """
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
        """
        Remove given node where node has two children.
        :param node:
        :return:
        """
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
    # bt.insert(75)
    # bt.insert(80)
    # bt.insert(60)
    # bt.insert(74)
    # bt.insert(73)
    # bt.insert(90)
    # bt.insert(58)
    bt.walk_in_order()
    print('***********************************************')
    bt.remove(50)
    bt.walk_in_order()
    # print('***********************************************')
