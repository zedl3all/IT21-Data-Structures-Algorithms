"""Parentheses Matching"""

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

def is_parentheses_matching():
    """is_parentheses_matching"""
    check = ArrayStack()
    parentheses = input()
    count = 0
    for i in parentheses:
        if i == "(":
            check.push(i)
        elif i == ")":
            if not check.pop():
                count += 1
    if count != 0 or check.data:
        print("Parentheses in", parentheses, "are unmatched")
        return False
    else:
        print("Parentheses in", parentheses, "are matched")
        return True

print(is_parentheses_matching())
