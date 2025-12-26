class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()
dog2.bark()
# Output: Buddy says Woof!
# Output: Max says Woof!