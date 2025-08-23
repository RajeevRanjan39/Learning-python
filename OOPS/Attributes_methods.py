class Student:
    # def __init__(self, a, b):
    #     self.roll_no = a
    #     self.name = b
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
    # Same as above

    def display(self):
        print(self.name, self.roll_no)

s0 = Student(42,'Rajeev')
s0.display()

s1 = Student(48, 'Arya')
s1.display()