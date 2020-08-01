
# first line python
print("hello world")

# variable
print(8 / 2 + 3 - 1)

a1 = (1 + 2) * 3 / 2 + 7
print(a1)

a1 = "a1 value"
print(a1)

int_var1 = 100
print(int_var1.bit_length())

print(10%3) # 1
print(10//3) # 3
print(10/3) # 3.3333333333333335 有误差
print(2**3) # 8

print(1 != 2)

str1 = '''abc
efh'''
print(str1)
str2 = """abc
efh"""
print(str2)
str3 = 'abc \
efh'
print(str3) # abc efh
str4 = "abc \
efh"
print(str4) # abc efh

print(type(str4)) # <class 'str'>

print('a' + 'b') # ab
print('a' * 3) # aaa

b1 = False
print(b1) # False
print(b1 == 0) # True

# a2 = input('please input:')
# print(a2)
# a3 = input('please input:')
# print(int(a3) + 5)

count = 5
while count > 2:
    print(count)
    count -= 1
else:
    print(count)

s1 = 'a'
s2 = 'aa'
print("%s - %s" % (s1, s2))
print("{} - {}".format(s1, s2))
print("{1} - {0}".format(s1, s2))
print("{var1} - {var2}".format(var1=s1, var2=s2))

str1 = "1234567890"
print(str1[2:4]) # 34
print(str1[3:]) # 4567890
print(str1[:])
print(str1[:5])
print(str1[-4:-2]) # 78
print(str1[2:6:2]) # 35

str2 = "abBc scc"
nstr2 = str2.capitalize()
print(nstr2) # Abbc
nstr3 = str2.upper()
nstr33 = str2.lower()
print(nstr3) # ABBC
print(nstr33) # abbc
s3 = str2.swapcase();
print(s3) # ABbC
s33 = str2.title()
print(s33) # Abbc Scc
s4 = str2.center(12, "*")
print(s4) # **abBc scc**
s5 = str2.strip()
s55 = str2.strip("b")
s51 = str2.lstrip()
s52 = str2.rstrip()
s54 = str2.replace('a', 'newa', 2)
s56 = str2.split(' ')
print(s56) # ['abBc', 'scc']
print(str2.startswith('a'))
print(str2.endswith('a'))
print(str2.count('a'))
print(str2.find('a'))
print(str2.index('a'))


print(str2.isdigit())
print(str2.isalpha())
print(str2.isalnum())
print(str2.isdecimal())
print(str2.isnumeric())

str2 = 'abc'
k = 0
while k < len(str2):
    print(str2[k])
    k += 1
print('------')
for c in str2:
    print(c)

print('b' in str2)
l1 = ['1', '2']
print('1' in l1)

l2 = [True, '1', 99, "abc", ['abc','1'], {"a":"b"}]
print(l2.index('1'))

m1 = {"a":1,"a":2}
print(m1)
m2 = {1:"a", True:1,(1,2):"bc"}
print(m2)
v1 = m2.popitem()
print(type(v1))
print(v1)

l2 = m2.keys()
print('l2',type(l2)) # l2 <class 'dict_keys'>
l3 = m2.values()

ss1 = ('abc')
print(type(ss1)) # <class 'str'>

for i in m2:
    print(i)
for i in m2.keys():
    print(i)
for i in m2.values():
    print(i)
for i in m2.items():
    print(i)
for i in m2.items():
    a,b = i
    print(a)
    print(b)
for a,b in m2.items():
    print(a)
    print(b)