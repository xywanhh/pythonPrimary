p = ('a', 'b')
print(type(p))
print(p[0])
print(p[1])

from collections import namedtuple
# namedtuple('名称', [属性list]):
Point = namedtuple('Point', ['name', 'age', 'y', 'z'])
p2 = Point('aa', 2, [1, 2], {3, 4})

print(type(p2.name))
print(p2.name)

print(type(p2.age))
print(p2.age)

print(type(p2.y))
print(p2.y)

print(type(p2.z))
print(p2.z)

# list
l1 = list([1, 2, 'a'])
print(l1)
l1.append((3, '4b'))
print(l1)
print(l1.pop())
print(l1)

from collections import deque
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# list是线性存储，数据量大的时候，插入和删除效率很低。
l2 = deque([1, 'a', [4, '9a'], {1, 2}])
print(l2)
l2.append({'a':1,'aa':2})
print(l2)
l2.appendleft('2222')
print(l2)
print(l2.pop())
print(l2)

from collections import OrderedDict
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
# dict
d1 = dict([('a', 1), ('b', 2), ('c', 3)])
d2 = {
    'a': 11,'b':'b2','c':'cc'
}
print(d1)
print(d2)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2']) # key2不存在，返回默认值

# 对list进行分组 {'k1': 大于66 , 'k2': 小于66}
# Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代
values = [11, 22, 33,44,55,66,77,88,99,90]
my_dict1 = {}
for value in  values:
    if value>66:
        if my_dict1.__contains__('k1'):
            my_dict1['k1'].append(value)
        else:
            my_dict1['k1'] = [value]
    else:
        if my_dict1.__contains__('k2'):
            my_dict1['k2'].append(value)
        else:
            my_dict1['k2'] = [value]
print(my_dict1)

values = [11, 22, 33,44,55,66,77,88,99,90]
my_dict2 = defaultdict(list)
for value in values:
    if value > 66:
        my_dict2['k1'].append(value)
    else:
        my_dict2['k2'].append(value)
print(my_dict2)

from collections import Counter
# Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。
c = Counter('abcdeabcdabcaba')
print(c)