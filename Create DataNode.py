"""Create DataNode"""

class DataNode:
    """Datanode"""
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    def get_data(self):
        """Get Data"""
        return self.__data

    def set_data(self, data):
        """Set data"""
        self.__data = data

    def get_next(self):
        """Get Next"""
        return self.__next

    def set_next(self, nexts):
        """Set Next"""
        self.__next = nexts

def main():
    """main"""
    object1 = DataNode(input())
    print(object1.get_data())
    print(object1.get_next())

main()
