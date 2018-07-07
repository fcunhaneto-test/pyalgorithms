def calculate_violation(self, parent):
    if parent.parent:
        print('parent:', parent.value)
        print('parent.parent:', parent.parent.value)
        self._fix_violation(parent.parent)

    if parent.parent and parent == parent.parent.left:
        fb = parent.height - parent.parent.right.height
        if fb > 1:
            if parent.parent == self.root:
                parent.parent.height -= 2

            self._rotate_right(parent.parent)

            if parent.parent.parent:
                parent.parent.parent.height -= 2
        if fb < -1:
            if parent.parent == self.root:
                parent.parent.height -= 2

            self._rotate_left(parent.parent)

            if parent.parent:
                parent.parent.height -= 2
    elif parent.parent and parent == parent.parent.right:
        fb = parent.parent.left.height - parent.height

        if fb > 1:
            if parent.parent == self.root:
                parent.parent.height -= 2

            self._rotate_right(parent.parent)

            if parent.parent:
                parent.parent.height -= 2
        elif fb < -1:
            if parent.parent == self.root:
                parent.parent.height -= 2

            self._rotate_left(parent.parent)

            if parent.parent:
                parent.parent.height -= 2

def calculate_violation(self, node, parent):

    if parent.parent and parent == parent.parent.left:
        fb = parent.height - parent.parent.right.height

        if fb > 1:
            if parent.parent == self.root:
                parent.parent.height -= 2
            print('************************************************')
            print('left rotate right')
            print('insert:', node.value, 'parent:', parent.value, 'parent.parent:', parent.parent.value)

            self._rotate_right(parent)

            if parent.parent:
                self._fix_violation(node, parent.parent)
                print('now parent:', parent.value)
            else:
                print('now parent:', None)
            print('************************************************')

            if parent.parent:
                parent.parent.height -= 2
        elif fb < -1:
            if parent.parent == self.root:
                parent.parent.height -= 2

            print('************************************************')
            print('left rotate left')
            print('insert:', node.value, 'parent:', parent.value, 'parent.parent:', parent.parent.value)
            # print('************************************************')

            self._rotate_left(parent.parent)

            if parent.parent:
                self._fix_violation(node, parent.parent)
                print('now parent:', parent.value)
            else:
                print('now parent:', None)
            print('************************************************')
            if parent.parent:
                parent.parent.height -= 2
    elif parent.parent and parent == parent.parent.right:

        fb = parent.parent.left.height - parent.height

        if fb > 1:
            if parent.parent == self.root:
                parent.parent.height -= 2

            print('************************************************')
            print('left rotate left')
            print('insert:', node.value, 'parent:', parent.value, 'parent.parent:', parent.parent.value)
            # print('************************************************')
            self._rotate_right(parent.parent)

            if parent.parent:
                self._fix_violation(node, parent.parent)
                print('now parent:', parent.value)
            else:
                print('now parent:', None)
            print('************************************************')

            if parent.parent:
                parent.parent.height -= 2
        elif fb < -1:
            if parent.parent == self.root:
                parent.parent.height -= 2

            print('************************************************')
            print('left rotate left')
            print('insert:', node.value, 'parent:', parent.value, 'parent.parent:', parent.parent.value)
            # print('************************************************')

            self._rotate_left(parent.parent)

            if parent.parent:
                self._fix_violation(node, parent.parent)
                print('now parent:', parent.value)
            else:
                print('now parent:', None)
            print('************************************************')

            if parent.parent:
                parent.parent.height -= 2
