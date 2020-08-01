import sys

#demo.py
import my_module #只在第一次导入时才执行my_module.py内代码,此处的显式效果是只打印一次'from the my_module.py',当然其他的顶级代码也都被执行了,只不过没有显示效果.
import my_module
import my_module
import my_module

'''
执行结果：
from the my_module.py
'''

# 当前已经加载的模块
# sys.modules是一个字典，内部包含模块名与模块对象的映射，该字典决定了导入模块时是否需要重新导入。
print(sys.modules)

#测试一:money与my_module.money不冲突
#demo.py
import my_module
money=10
print(my_module.money)

'''
执行结果：
from the my_module.py
1000
'''

#测试二：read1与my_module.read1不冲突
#demo.py
import my_module
def read1():
    print('========')
my_module.read1()

'''
执行结果:
from the my_module.py
my_mo
'''

#测试三：执行my_module.change()操作的全局变量money仍然是my_module中的
#demo.py
import my_module
money=1
my_module.change()
print(money)

'''
执行结果：
from the my_module.py
1
'''

# 内建函数dir是用来查找模块中定义的名字，返回一个有序字符串列表
d1 = dir(my_module)
print(d1)

# dir()不会列举出内建函数或者变量的名字，它们都被定义到了标准模块builtin中，可以列举出它们
import builtins
d2 = dir(builtins)
print(d2)