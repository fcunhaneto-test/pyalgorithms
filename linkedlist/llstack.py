"""
A linked list implementation as stack.
"""


class Node:
    """
    Implement a node for linked list.

    Attributes:
        data: the node data.
        _next: the next node from this node
    """
    def __init__(self, data):
        self._data = data
        self._next = None


class LLQueue(Node):
    """
    Implement linked list as stack.

     Attributes:
        _head: point to head in linked list.
        _size: the size of liked list.
    """
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, data):
        """
        Insert node in linked list.

        :param
            data: the node data.
        """
        nodo = Node(data)

        if self.is_empty():
            self._head = nodo
        else:
            current = self._head
            nodo._next = current
            self._head = nodo

        self._size += 1

    def pop(self):
        """
        Remove and return the __vertices in reverse order they were insert.

        :return:
           _data (AVLNode): the data in the node.
        """
        if self.is_empty():
            return None

        nodo = self._head
        self._head = nodo._next
        data = nodo._data
        nodo = Node(None)

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
        current = self._head
        yield current._data
        while current._next:
            current = current._next
            yield current._data


    def __len__(self):
        """
        Return size of linked list.

        :return:
            _size (LLStack): size of linked list
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
    print(ll.pop())
    # print(ll.pop())
    # print(ll.pop())
    # print(ll.pop())
    # print(ll.pop())
    print('********************')
    for x in ll:
        print(x)
    print('********************')
    # print(len(ll))
