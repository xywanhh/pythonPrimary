import re

# re模块下的常用方法
ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果,放在列表里
print(ret) #结果 : ['a', 'a']

ret = re.search('a', 'eva egon yuan').group()
print(ret) #结果 : 'a'
# 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

ret = re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配
print(ret)
#结果 : 'a'

ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']

ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret)

obj = re.compile('\d{3}')  #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group())  #结果 ： 123

ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
print(ret)  # <callable_iterator object at 0x10195f940>
print(next(ret).group())  #查看第一个结果
print(next(ret).group())  #查看第二个结果
print([i.group() for i in ret])  #查看剩余的左右结果

# findall的优先级查询：
ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['oldboy']     这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可

ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
print(ret)  # ['www.oldboy.com']

# split的优先级查询
ret=re.split("\d+","eva3egon4yuan")
print(ret) #结果 ： ['eva', 'egon', 'yuan']

ret=re.split("(\d+)","eva3egon4yuan")
print(ret) #结果 ： ['eva', '3', 'egon', '4', 'yuan']
#在匹配部分加上（）之后所切出的结果是不同的，
#没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项，
#这个在某些需要保留匹配部分的使用过程是非常重要的。


# 匹配整数
ret=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) #['1', '2', '60', '40', '35', '5', '4', '3']
ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) #['1', '-2', '60', '', '5', '-4', '3']
ret.remove("")
print(ret) #['1', '-2', '60', '5', '-4', '3']

# 匹配标签
ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
#还可以在分组中利用?<name>的形式给分组起名字
#获取的匹配结果可以直接用group('名字')拿到对应的值
print(ret.group('tag_name'))  #结果 ：h1
print(ret.group())  #结果 ：<h1>hello</h1>

ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
#如果不给组起名字，也可以用\序号来找到对应的组，表示要找的内容和前面的组内容一致
#获取的匹配结果可以直接用group(序号)拿到对应的值
print(ret.group(1))
print(ret.group())  #结果 ：<h1>hello</h1>
