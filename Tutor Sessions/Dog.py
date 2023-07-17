class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("woof")

    def run(self):
        print(self.name + " is running")

class Bulldog(Dog):
    def __init__(self,name, breed):
        # self.breed = "bulldog"
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print("wooh")

    def Stroke(self):
        print("stroking " + self.name)