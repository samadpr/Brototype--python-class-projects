"""
class BaseClass:
    def display(self):
        print("Hello...")



class subClass(BaseClass):
    def welcome(self):
        print("welcome")


x=BaseClass()
x.display()

y=subClass()
y.display()
y.welcome()
"""

"""
class BaseClass:
    def set_Name(self,Name):
        self.Name=Name

class subClass(BaseClass):
    def welcome(self):
        print("welcome")

    def display_Name(self):
        print("Name : " + self.Name)



y=subClass()
y.welcome()
y.set_Name("Abdul samad")
y.display_Name()
"""

#consecter
class BaseClass:
    def __init__(self):
        print("Base init")

    def set_Name(self,Name):
        self.Name=Name
        print("Base Class set name")

class subClass(BaseClass):

    def __init__(self):
       # BaseClass.__init__(self) or
        super().__init__()
        print("SubClass init")

    def set_Name(self,Name):
        #self.Name=Name
        super().set_Name(Name)
        print("Subclass set name")

    def welcome(self):
        print("welcome")

    def display_Name(self):
        print("Name : " + self.Name)



y=subClass()
y.welcome()
y.set_Name("Abdul samad")
y.display_Name()