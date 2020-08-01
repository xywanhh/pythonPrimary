def f1():
    print('f1 call')

def f2():
    print("f2 call")
    return 123

def f3():
    return 123
    print("f3 call")

def f4():
    print("def f4")
    return 123
    print("f2 call")

def f5():
    return 123, 456

def f6(a, b):
    print("{} - {}".format(a, b))

def f7(a, b='b'):
    print("{} - {}".format(a, b))

def f8(*args, b='b'):
    print(type(args))
    print("{} - {}".format(args, b))

def f9(a = '1', *args, b='b'):
    print('a:', a)
    print('args:', args)
    print('b:', b)

def f10(a = '1', *args, b='b', **kargs):
    print('a:', a)
    print('args:', args)
    print('b:', b)
    print('kargs:', kargs)

f1()
print(f2())
print(f3()) # 123
print(f4())
print(f5()) # (123, 456)
f6(1, 2)
f6(b=1, a=2)
f7(1)
f8((1,), 22)
f8(111, b=22)
f9()
f10()