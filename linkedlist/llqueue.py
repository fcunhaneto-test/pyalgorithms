"""
A linked list implementation as stack.
"""


class Node:
    """
    Implement a node for linked list.

    Attributes:
        _data: the node data.
        _previ: the previous node from this node
    """
    def __init__(self, data):
        self._data = data
        self._previ = None


class LLQueue(Node):
    """
    Implement linked list as queue.

    Attributes:
        _head: point to head in linked list.
        _tail: point to tail in linked list.
        _size: the size of liked list.
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def push(self, data):
        """
        Insert node in linked list.

        Args:
            data: the node data.
        """
        nodo = Node(data)

        if self.is_empty():
            self._head = nodo
            self._tail = nodo
        elif self._size == 1:
            current = self._head
            current._previ = nodo
            self._tail = current
            self._head = nodo

        else:
            current = self._head
            current._previ = nodo
            self._head = nodo

        self._size += 1

    def pop(self):
        """
        Remove and return the vertices in order they were insert.

        :return:
           _data (AVLNode): the data in the node.
        """
        if self.is_empty():
            return None

        nodo = self._tail
        self._tail = nodo._previ
        data = nodo._data
        nodo = None

        self._size -= 1

        return data

    def show(self):
        """
        Show all node data in linked list.
        """
        current = self._tail
        print(current._data)
        while current._previ:
            current = current._previ
            print(current._data)

    def is_empty(self):
        """
        Check if the linked list is empty.

        :return:
            boolean: (True if is empty else False)
        """
        if self._size == 0:
            return True
        return False

    def __iter__(self):
        """
        Iterate from the linked list.

        :return:
            _data (AVLNode): the data in current node in iterator.
        """
        if self.is_empty():
            raise StopIteration
        current = self._tail
        yield current._data
        while current._previ:
            current = current._previ
            yield current._data

    def __len__(self):
        """
        Return size of linked list.

        :return:
            _size (LLQueue): size of linked list
        """
        return self._size

if __name__ == '__main__':
    ll = LLQueue()
    ll.push(15)
    ll.push(11)
    ll.push(6)
    ll.push(8)
    for x in ll:
        print(x)
    print('********************')
    print(ll.pop())
    print('********************')
    for x in ll:
        print(x)
    print('********************')

