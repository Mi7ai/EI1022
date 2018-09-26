class Person:
    __slots__ = ('name','age')
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def last_name(self):
        return self.name.split()[-1]

somebody = Person('Juan Nadie',35)
print(somebody.name, somebody.age)
print('Last name:', somebody.last_name())