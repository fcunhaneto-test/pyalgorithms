"""
A implement a doubly linked.
"""


class Node:
    """
    Implement a node for linked list.

    Attributes:
        data: the node data.
        _next: the next node from this node
        _previ: the previous node from this node
    """
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previ = None


class DoublyLL(Node):
    """
    Implement linked list as queue.

     Attributes:
        _head: point to head in linked list.
        _tail: point to tail in linked list.
        _size: the size of liked list.
        __gnext: generator for linked list who iterate from head to tail.
        __gprevi: generator for linked list who iterate from tail to head.

    Example:
        >>> ll = DoublyLL()
        >>> ll.push_head(5)
        >>> ll.push_head(6)
        >>> ll.push_head(7)
        >>> ll.push_head(8)
        >>> ll.show()
        8
        7
        6
        5
        >>> ll.push_tail(1)
        >>> ll.push_tail(2)
        >>> for x in ll: print(x)
        8
        7
        6
        5
        1
        2
        >>> print(ll.pop_head())
        8
        >>> print(ll.pop_tail())
        2
        >>> print(ll.pop_tail())
        1
        >>> for x in ll: print(x)
        7
        6
        5
        >>> print(ll.get_next())
        7
        >>> print(ll.get_next())
        6
        >>> print(ll.get_next())
        5
        >>> print(ll.get_previ())
        5
        >>> print(ll.get_previ())
        6
        >>> print(ll.get_previ())
        7
        >>> ll.restart_gprevi()
        >>> print(ll.get_previ())
        5
        >>> print(ll.get_previ())
        6
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        self.__gnext = self.__forward()
        self.__gprevi = self.__backward()

    def __init_ll(self, node):
        if self.is_empty():
            self._head = node
            self._tail = node
        elif self._size == 1:
            current = self._head
            self._head = node
            node._next = current
            current._previ = node
            self._tail = current

    def push_head(self, data):
        """
        Insert node in the head of linked list.

        Args:
            data: the node data.
        """
        node = Node(data)

        if self.is_empty() or self._size == 1:
            self.__init_ll(node)
        else:
            current = self._head
            current._previ = node
            node._next = current
            self._head = node


        self._size += 1

    def push_tail(self, data):
        """
        Insert node in the tail of linked list.

        Args:
            data: the node data.
        """
        node = Node(data)

        if self.is_empty() or self._size == 1:
            self.__init_ll(node)
        else:
            current = self._tail
            current._next = node
            node._previ = current
            self._tail = node

        self._size += 1

    def pop_head(self):
        """
        Remove the node in the head and return it's data.

        Returns:
           _data (Node): the data in the node.
        """
        if self.is_empty():
            return None

        current = self._head._next
        node = self._head
        current._previ = None
        self._head = current
        data = node._data
        nodo = Node(None)

        self._size -= 1

        return data

    def pop_tail(self):
        """
        Remove the node in the tail and return it's data.

        Returns:
           _data (Node): the data in the node.
        """
        if self.is_empty():
            return None

        current = self._tail._previ
        node = self._tail
        current._next = None
        self._tail = current
        data = node._data
        node = Node(None)

        self._size -= 1

        return data

    def show(self):
        """
        Show all node data in linked list.
        """
        current = self._head
        print(current._data)
        while current._next:
            current = current._next
            print(current._data)

    def is_empty(self):
        """
        Check if the linked list is empty.

        Returns:
            boolean: (True if is empty else False)
        """
        if self._size == 0:
            return True
        return False

    def get_next(self):
        """
        Get the next node data from head to tail.

        Returns:
            data (Node): the data in current node
        """
        try:
            g = next(self.__gnext)
        except StopIteration:
            return None

        return g

    def get_previ(self):
        """
        Get the next node data from tail to head.

        Returns:
            data (Node): the data in current node
        """
        try:
            g = next(self.__gprevi)
        except StopIteration:
            return None

        return g

    def restart_gnext(self):
        """
        Restart get_next.
        """
        self.__gnext = self.__forward()

    def restart_gprevi(self):
        """
        Restart get_previ.
        """
        self.__gprevi = self.__backward()

    def __forward(self):
        """
       Iterate from head node to tail node in linked list.

       Returns:
           data (Node): the data in current node in iterator.
       """
        if self.is_empty():
            raise StopIteration

        current = self._head
        yield current._data
        while current._next:
            current = current._next
            yield current._data

    def __backward(self):
        """
        Iterate from first node to last node in linked list.

        Returns:
            data (Node): the data in current node in iterator.
        """
        if self.is_empty():
            raise StopIteration

        current = self._tail
        yield current._data
        while current._previ:
            current = current._previ
            yield current._data

    def __iter__(self):
        """
        Iterate from the linked list.

        Returns:
            _data (Node): the data in current node in iterator.
        """
        if self.is_empty():
            raise StopIteration
        current = self._head
        yield current._data
        while current._next:
            current = current._next
            yield current._data

    def __len__(self):
        """
        Return size of linked list.

        Returns:
            _size (LLQueue): size of linked list
        """
        return self._size

if __name__ == '__main__':
    ll = DoublyLL()
    ll.push_head(5)
    ll.push_head(6)
    ll.push_head(7)
    ll.push_head(8)
    ll.show()
    print('********************')
    ll.push_tail(1)
    ll.push_tail(2)
    print('after push_tail')
    for x in ll:
        print(x)
    print('********************')
    print(ll.pop_head())
    print(ll.pop_tail())
    print(ll.pop_tail())
    print('********************')
    print('after pop head and tail')
    for x in ll:
        print(x)
    print('********************')
    print(ll.get_next())
    print(ll.get_next())
    print(ll.get_next())
    print('********************')
    print(ll.get_previ())
    print(ll.get_previ())
    print(ll.get_previ())
    print('********************')
    ll.restart_gprevi()
    print(ll.get_previ())
    print(ll.get_previ())
    print('********************')
    # import doctest
    #
    # doctest.testmod()
    print(ll.__doc__)

