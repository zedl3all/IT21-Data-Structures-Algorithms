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
    def __init__(self, count=0, head=DataNode()):
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

    def insert_front(self, data):
        """insert_front"""
        insertfront = DataNode()
        insertfront.set_data(data)
        if self.head.get_data() is None:
            pass
        else:
            insertfront.set_next(self.head)
        self.head = insertfront

    def insert_before(self, node, data):
        """insert_Before"""
        this = DataNode()
        this.set_data(data)
        if self.head is None: # ใช้ insert_before ในขนาดที่ไม่มีข้อมูลอยู่
            print("Cannot insert, %s does not exist." % node)
        else:
            current_object = self.head
            first = None
            while current_object.get_next() is not None:
                if current_object.get_data() == node:
                    break
                first = current_object
                current_object = current_object.get_next()
            if current_object.get_data() != node:
                print("Cannot insert, %s does not exist." % node)
            else:
                if first is None: # หากตัวที่ต้องการแทรกเป็นตัวแรก
                    self.head = this
                else:
                    first.set_next(this)
                this.set_next(current_object)

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
for _ in range(int(input())):
    TEXT_ = input()
    CONDI_, DATA_ = TEXT_.split(": ")
    if CONDI_ == "F":
        LIST1_.insert_front(DATA_)
    elif CONDI_ == "L":
        LIST1_.insert_last(DATA_)
    elif CONDI_ == "B":
        LIST1_.insert_before(*DATA_.split(", "))
    else:
        print("Invalid Condition!")
LIST1_.traverse()
