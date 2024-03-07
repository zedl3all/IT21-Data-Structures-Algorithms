"""Person V.2 (Class)"""

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

class Project:
    """Project"""
    def __init__(self, name, nummembers):
        """init"""
        self.name = name
        self.nummembers = nummembers

    def showprojectname(self):
        """show project name"""
        print("Hello There! This is %s" % self.name)

    def showmembers(self):
        """show member"""
        print("This project has %s members" % self.nummembers)

def run():
    """run"""
    projectname = input()
    member = int(input())
    allmember = []
    for _ in range(member):
        prememver = [input(), int(input())]
        allmember.append(prememver)
    allmember.sort(key=lambda x: x[0])
    data1 = Project(projectname, member)
    data1.showprojectname()
    data1.showmembers()
    for i in range(len(allmember)):
        data2 = Person(allmember[i][0], allmember[i][1])
        data2.say_hello()
run()
