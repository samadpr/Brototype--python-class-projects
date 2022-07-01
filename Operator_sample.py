class sample:
    def set_name(self,name):
        self.name=name

    def __add__(self, other):
        name=self.name+" "+other.name
        return name


first_name=sample()
second_neme=sample()

first_name.set_name("Abdul")
second_neme.set_name("Samad")

full_name=first_name+second_neme
print(full_name)



