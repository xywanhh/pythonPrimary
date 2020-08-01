class Foo:
    def __init__(self,val):
        self.__NAME=val #将所有的数据属性都隐藏起来

    @property
    def name(self):
        return self.__NAME #obj.name访问的是self.__NAME(这也是真实值的存放位置)

    @name.setter
    def name(self,value):
        if not isinstance(value,str):  #在设定值之前进行类型检查
            raise TypeError('%s must be str' %value)
        self.__NAME=value #通过类型检查后,将值value存放到真实的位置self.__NAME

    @name.deleter
    def name(self):
        raise TypeError('Can not delete')

f=Foo('egon')
print(f.name)
f.name = 'www'
print(f.name)
# f.name=10 #抛出异常'TypeError: 10 must be str'
# del f.name #抛出异常'TypeError: Can not delete'

class Foo:
    def get_AAA(self):
        print('get的时候运行我啊')

    def set_AAA(self,value):
        print('set的时候运行我啊')

    def delete_AAA(self):
        print('delete的时候运行我啊')
    AAA=property(get_AAA,set_AAA,delete_AAA) #内置property三个参数与get,set,delete一一对应

f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA