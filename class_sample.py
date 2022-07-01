"""
class MySampleClass:
    def hello(self):
        print("hello ")


x = MySampleClass()
x.hello()  # or  MySampleClass.hello(x)
"""
"""
class MySampleClass:
    def hello(self,name):
        print("hello \n"+name)


x = MySampleClass()
name="Abdul Samad"
x.hello(name)  # or  MySampleClass.hello(x)
"""

"""
class MySampleClass:
    def hello(self, name):
        self.na = name

    def print_name(self):
        print(self.na)


x = MySampleClass()
y = MySampleClass()
name = "Abdul Samad "
x.hello(name)
y.hello("my dear")

x.print_name()
y.print_name()
"""


class CrossRoadsTeamMember:
    year = 2021

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year : " + str(CrossRoadsTeamMember.year))
        print("Name : " + self.name)
        print("Age  : " + str(self.age))
        print("Place: " + self.place)

    @classmethod
    def add_year(cls):
        cls.year = cls.year + 1

    @staticmethod
    def display_welcome():
        print("*Welcome* \n")



CrossRoadsTeamMember.display_welcome()

x = CrossRoadsTeamMember("Abdul samad", 18, "kunnamkulam \n")
y = CrossRoadsTeamMember("Abdul Rahman", 18, "pukkattupade")

x.display()
y.display()

print("___________________________________")

CrossRoadsTeamMember.year = CrossRoadsTeamMember.year + 1
x.add_age()
y.add_age()

x.display()
y.display()

print("___________________________________")

CrossRoadsTeamMember.add_year()

x.add_age()
y.add_age()
x.relocate("calicut \n")
y.relocate("mumbai")

x.display()
y.display()

print("___________________________________")

CrossRoadsTeamMember.add_year()

x.add_age()
y.add_age()
x.relocate("bahrain \n")
y.relocate("mumbai")

x.display()
y.display()


print("___________________________________")

CrossRoadsTeamMember.add_year()

x.add_age()
y.add_age()
x.relocate("Qather \n")
y.relocate("cheramangade")

x.display()
y.display()