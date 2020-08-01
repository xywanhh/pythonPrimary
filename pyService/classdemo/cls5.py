class Animal:
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity  # 人和狗都有自己的攻击力;
        self.life_value = life_value  # 人和狗都有自己的生命值;

    def eat(self):
        print('%s is eating'%self.name)

class Dog(Animal):
    '''
    狗类，继承Animal类
    '''
    def bite(self, people):
        '''
        派生：狗有咬人的技能
        :param people:  
        '''
        people.life_value -= self.aggressivity

class Person(Animal):
    '''
    人类，继承Animal
    '''
    def attack(self, dog):
        '''
        派生：人有攻击的技能
        :param dog: 
        '''
        dog.life_value -= self.aggressivity

egg = Person('egon',10,1000)
ha2 = Dog('二愣子',50,1000)
print(ha2.life_value)
print(egg.attack(ha2))
print(ha2.life_value)