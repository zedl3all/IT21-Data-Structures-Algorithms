"""Person"""

class Person:
    """Person"""
    def __init__(self, name, age):
        """init"""
        self.name = name
        self.age = age

    def get_details(self):
        """detail"""
        print("%s, %s years old" % (self.name, self.age))

    def say_hello(self):
        """say hello"""
        print("Hello, my name is %s!" % self.name)

def run():
    """runprogram"""
    persondata = Person(input(), int(input()))
    persondata.get_details()
    persondata.say_hello()

run()
