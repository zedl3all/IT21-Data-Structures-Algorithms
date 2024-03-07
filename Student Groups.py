"""Student Groups"""

class ArrayStack:
    """stack"""
    def __init__(self, size=0, data=None):
        """init"""
        if data is None:
            data = []
        self.size = size
        self.data = data

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """pop"""
        try:
            last = self.data[-1]
            self.data = self.data[:-1]
            self.size -= 1
            return last
        except IndexError:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """empty"""
        if self.size <= 0:
            return True
        else:
            return False

    def get_stack_top(self):
        """get stack top"""
        if self.is_empty() is True:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            return self.data[-1]

    def get_size(self):
        """getsize"""
        return self.size

    def print_stack(self):
        """print stack"""
        print(self.data)

def main():
    """main"""
    group = int(input())
    people = int(input())
    allpeople = []
    allgroup = []
    for _ in range(people):
        allpeople.append(input())
    for _ in range(group):
        allgroup.append([])
    student = ArrayStack(data=allgroup)
    count = 0
    for _ in range(people):
        if count == group:
            count = 0
        student.data[count].append(allpeople.pop())
        count += 1
    for number, name in enumerate(student.data):
        name = str(name)
        name = name.replace("'", "")
        name = name[1:-1]
        #print(number,name)
        print("Group", str(number+1)+":", name)

main()
