import random

# 大于0且小于1之间的小数
r1 = random.random()
print(r1)

#大于1小于3的小数
r2 = random.uniform(1, 3)
print(r2)

# 大于等于1且小于等于5之间的整数
r3 = random.randint(1, 5)
print(r3)

# 大于等于1且小于10之间的奇数
r4 = random.randrange(1, 10, 2)
print(r4)

# 随机选择一个返回
r5 = random.choice([1, 'a', [2, (2, '3a')]])
print(r5)

# 随机选择多个返回，返回的个数为函数的第二个参数
r6 = random.sample([1, 'a', [2, (2, '3a')]], 2)
print(r6)

# 打乱列表顺序
item=[1,3,5,7,9]
print(item)
random.shuffle(item)
print(item)

# 生成随机验证码
def v_code():
    code = ''
    for i in range(5):
        ret = list(str(j) for j in range(0, 10)) + list(chr(i) for i in range(65,91))
        add = random.choice(ret)
        code = "".join([code,str(add)])
    return code

# ret = list(str(j) for j in range(0, 10)) + list(chr(i) for i in range(65,91))
# print(ret)
print(v_code())