
def Person(*args, **kwargs):
    self = {}
    def read(self):
        print("%s is reading." % self['name'])
    def __init__(name):
        self['name'] = name
        self['read'] = read
    __init__(*args, **kwargs)
    return self

class Person1:
    def read(self):
        print("%s is reading." % self.name)
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    p1 = Person('p1')
    p1['read'](p1)
    p2 = Person1('p2')
    p2.read()