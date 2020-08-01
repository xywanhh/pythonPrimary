
class Person:
    def read(self):
        print("%s is reading." % self.name)
    def __init__(self, name):
        self.name = name
        self.animal = Animal()

class Animal:
    def eat(self):
        print("eating food.")

if __name__ == '__main__':
    p1 = Person('p1')
    p1.read()
    p1.animal.eat()