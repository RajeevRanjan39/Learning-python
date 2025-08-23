class Student:
    # def __init__(self, a, b):
    #     self.roll_no = a
    #     self.name = b
    def __init__(self, roll_no, name, total):
        self.roll_no = roll_no
        self.name = name
        self.total = total
    # Same as above

    def display(self):
        print(self.name, self.roll_no)

    def result(self):
        if self.total > 120:
            print('Pass')
        else:
            print('Fail')

s0 = Student(42,'Rajeev',125)
s0.display()
s0.total()

s1 = Student(48, 'Arya',105)
s1.display()
s1.total()
