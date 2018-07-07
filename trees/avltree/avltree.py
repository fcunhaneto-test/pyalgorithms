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

            self._calculate_height(node)
            self._fix_violation(node)

        return True

    def _calculate_height(self, node):
        current = node

        while current:
            current.height = max(current.left.height, current.right.height) + 1
            current = current.parent

    def _fix_violation(self, node):
        previous = node
        current = node.parent

        while current:
            fb1 = current.left.height - current.right.height
            fb2 = previous.left.height - previous.right.height
            if fb1 >= 2 and fb2 >= 0:
                self._rotate_right(current)
                current.height -= 2
                self._calculate_height(current)
                break
            if fb1 <= -2 and fb2 <= 0:
                self._rotate_left(current)
                current.height -= 2
                self._calculate_height(current)
                break
            if fb1 >= +2 and fb2 <= 0:
                self._rotate_left(previous)
                previous.height -= 2
                self._calculate_height(previous)
                self._rotate_right(current)
                current.height -= 2
                self._calculate_height(current)
                break
            if fb1 <= -2 and fb2 >= 0:
                self._rotate_right(previous)
                previous.height -= 2
                self._calculate_height(previous)
                self._rotate_left(current)
                current.height -= 2
                self._calculate_height(current)
                break
            previous = current
            current = current.parent

    def _rotate_left(self, x):
        y = x.right
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

    def _rotate_right(self, x):
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
        """
        Remove node where key is equal of given value.
        :param value: numeric
        """
        print(value)
        node = self.search(value)

        if node == self.root:
            return self._remove_root()
        elif node.left == self.leaf and node.right == self.leaf:
            return self._remove_if_leaf(node)
        elif (node.left == self.leaf) ^ (node.right == self.leaf):
            return self._remove_if_one_child(node)
        else:
            return self._remove_if_two_children(node)

    def _remove_if_leaf(self, node):
        remove_key = node.key
        parent = node.parent
        if parent.left == node:
            parent.left = self.leaf
        else:
            parent.right = self.leaf

        self._calculate_height(parent)
        self._fix_violation(parent)

        del node

    def _remove_if_one_child(self, node):
        remove_key = node.key
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

        self._calculate_height(node.parent)
        self._fix_violation(node.parent)

        del node

    def _remove_if_two_children(self, node):
        remove_key = node.key
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

        self._calculate_height(node.parent)
        self._fix_violation(node.parent)

        del node

        return remove_key, successor.key

    def _remove_root(self):
        remove_key = self.root.key
        successor = None
        if self.root.left == self.leaf and self.root.right == self.leaf:
            self.root = None
        elif (self.root.left == self.leaf) ^ (self.root.right == self.leaf):
            if self.root.left != self.leaf:
                self.root = self.root.left
            else:
                self.root = self.root.right

            self.root.parent = None
        else:
            successor = self.successor(self.root.key)
            if successor == self.root.right:

                successor.parent = None
                successor.left = self.root.left
                self.root.left.parent = successor
                self.root = successor
            else:
                if successor.right:
                    successor.right.parent = successor.parent

                successor.parent.left = successor.right
                successor.left = self.root.left
                successor.right = self.root.right

                self.root.left.parent = successor
                self.root.right.parent = successor
                successor.parent = None
                self.root = successor

        self._calculate_height(self.root)
        self._fix_violation(self.root)


if __name__ == '__main__':
    # from trees import handletrees
    # handletrees.handle_trees()
    bt = AVLTree()
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    bt.insert(44)
    bt.insert(17)
    bt.insert(78)
    bt.insert(32)
    bt.insert(50)
    bt.insert(88)
    bt.insert(48)
    bt.insert(62)
    bt.insert(84)
    bt.insert(92)
    bt.insert(80)
    bt.insert(82)
    bt.walk_in_order()
    print('***********************************************')
    bt.remove(78)
    print('remove 78')
    print('node\tparent\tleft\tright\theight\tfb')
    print('***********************************************')
    bt.walk_in_order()
    print('***********************************************')

