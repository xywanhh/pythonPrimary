from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta): #同一类事物:动物
    @abstractmethod
    def talk(self):
        pass

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')

p1 = People().talk()
d1 = Dog().talk()
pig1 = Pig().talk()