class Teacher:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def teach(self):
        print('teaching')

class Professor(Teacher):
    pass

p1=Professor('egon','male')
p1.teach()
# teaching