"""Create DataNode"""

class DataNode:
    """Datanode"""
    def __init__(self, data=None):
        """init"""
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

class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self, count="0", head=DataNode()):
        """init"""
        self.count = count
        self.head = head

    def insert_last(self, data):
        """insert_last"""
        current_object = self.head
        if current_object.get_data() is None:
            current_object.set_data(data)
        else:
            insertlast = DataNode()
            insertlast.set_data(data)
            while True:
                if current_object.get_next() is None:
                    #current_object.set_data(data)
                    current_object.set_next(insertlast)
                    #print("data = ", current_object.get_data())
                    #print("next = ", current_object.get_next())
                    break

                current_object = current_object.get_next()

    def traverse(self):
        """traverse"""
        current_object = self.head
        if current_object.get_data() is None:
            print("This is an empty list.")
        else:
            while current_object is not None:
                print(current_object.get_data(), end="")
                if current_object.get_next() is not None:
                    print(" -> ", end="")
                current_object = current_object.get_next()

LIST1_ = SinglyLinkedList()
for i in range(int(input())):
    LIST1_.insert_last(input().strip())
LIST1_.traverse()
