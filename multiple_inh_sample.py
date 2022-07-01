
class First:
    def display(self):
        print("First")


class Second:
    def display(self):
        print("Second")


class Third(Second,First):
    def display_third(self):
        print("Third")


x = Third()
#x.display_third()
x.display()

print(Third.mro()) # MRO full form:-Method Resolution Order


"""
#multiple inheritence
class First:
    def display_first(self):
        print("First")


class Second(First):
    def display_second(self):
        print("Second")


class Third(Second):
    def display_third(self):
        print("Third")


x = Third()
x.display_third()
x.display_first()
"""