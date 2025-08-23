from person import person

class Student(person):
    def __init__(self,name,age, marks):
        super().__init__(name,age)
        # This is called inheritance, taking properties of parent class (person)
        self.marks = marks

    def display(self):
        super().display()
        # This is called inheritance, taking properties of parent class (person)
        print(self.marks)