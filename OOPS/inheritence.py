# in this program, we have learned to using inheritance and methods overriding

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(person):
    def __init__(self,name,age, marks):
        super().__init__(name,age)
        # This is called inheritance, taking properties of parent class (person)
        self.marks = marks

    def display(self):
        super().display()
        # This is called inheritance, taking properties of parent class (person)
        print(self.marks)

class Employee(person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary = salary

    def display(self):
        print(self.name, self.age,self.salary)
        # This is called method overrinding, instead of using inheritance 


s = Student('Rita', 20, 250)
s.display()

e = Employee('Rajeev', 20, 500000)
e.display()