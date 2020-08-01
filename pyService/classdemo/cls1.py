
def person(name, age):
    def read1(obj):
        print("%s is reading book." % obj['name'])
    data = {
        'name':name,
        'age':age,
        'read':read1
    }
    return data

def dog(name):
    def eat(obj):
        print("%s is eating." % obj['name'])
    return {
        'name':name,
        'eat':eat
    }

def read(obj):
    print("%s is reading book." % obj['name'])

if __name__ == '__main__':
    p = person('person1', 12)
    print(p['name'], p['age'])
    d = dog('dog1')
    print(d['name'])
    read(p)
    read(d)
    print(d['eat'](p))