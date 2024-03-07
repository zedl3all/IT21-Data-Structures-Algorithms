"""Create BSTNode"""

class BSTNode():
    """Create BSTNode"""
    def __init__(self, data, left=None, right=None):
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

def main():
    """main"""
    bi1 = BSTNode(data=int(input()))
    print(bi1.get_data())
    print(bi1.get_left())
    print(bi1.get_right())
main()
