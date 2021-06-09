class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID


s = Student('Qazi', 25, 1444)

print(s.age)
print(s.ID)
print(s.name)
