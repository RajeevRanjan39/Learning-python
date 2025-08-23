class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.__age = age
        # adding '__' before age will stopped from inherited to next like above

    def display(self):
        print(self.name, self.age)