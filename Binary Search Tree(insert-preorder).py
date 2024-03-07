"""Create BSTNode"""

class BSTNode():
    """Create BSTNode"""
    def __init__(self, data=None, left=None, right=None):
        """init"""
        self.data = data
        self.left = left
        self.right = right

    def get_data(self):
        """getdata"""
        return self.data
    def set_data(self, data):
        """setdata"""
        self.data = data
    def get_left(self):
        """getleft"""
        return self.left
    def set_left(self, left):
        """setleft"""
        self.left = left
    def get_right(self):
        """getright"""
        return self.right
    def set_right(self, right):
        """setright"""
        self.right = right

class BST():
    """BST"""
    def __init__(self, root=None):
        """init"""
        self.root = root

    def get_root(self):
        """get root"""
        return self.root

    def set_root(self, root):
        """set root"""
        self.root = root

    def insert(self, data):
        """insertdata"""
        if self.root is None:
            self.root = BSTNode(data)
        else:
            pointer = self.root
            while True:
                if data < pointer.get_data():
                    if pointer.get_left() is None:
                        node = BSTNode(data)
                        pointer.set_left(node)
                        break
                    else:
                        pointer = pointer.get_left()
                else:
                    if pointer.get_right() is None:
                        node = BSTNode(data)
                        pointer.set_right(node)
                        break
                    else:
                        pointer = pointer.get_right()

    def preorder(self):
        """preorder"""
        current = self.root

        while current:
            if current.get_left() is None:
                print(" -> %s"%current.get_data(), end="")
                current = current.get_right()
            else:
                predecessor = current.get_left()

                while (predecessor.get_right() is not None) and \
                    (predecessor.get_right() != current):
                    predecessor = predecessor.get_right() 

                if predecessor.get_right() is None:
                    print(" -> %s"%current.get_data(), end="")
                    predecessor.set_right(current)
                    current = current.get_left()
                else:
                    predecessor.set_right(None)
                    current = current.get_right()

    def inorder(self):
        """inorder"""
        current = self.root

        while current:
            if current.get_left() is None:
                print(" -> %s"%current.get_data(), end="")
                current = current.get_right()
            else:
                predecessor = current.get_left()

                while (predecessor.get_right() is not None) and \
                    (predecessor.get_right() != current):
                    predecessor = predecessor.get_right()

                if predecessor.get_right() is None:
                    predecessor.set_right(current)
                    current = current.get_left()
                else:
                    predecessor.set_right(None)
                    print(" -> %s"%current.get_data(), end="")
                    current = current.get_right()

    def postorder(self):
        """Postorder"""
        def _postorder(node):
            """Postorder"""
            if node:
                _postorder(node.get_left())
                _postorder(node.get_right())
                print(" -> %s"%node.get_data(), end="")
        _postorder(self.root)
        print()

    def is_empty(self):
        """isempty?"""
        return self.root is None

    def traverse(self):
        """tracerse"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder:', end='')
        self.preorder()
        print()
        print('Inorder:', end='')
        self.inorder()
        print()
        print('Postorder:', end='')
        self.postorder()
        print()

def main():
    """main"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()
