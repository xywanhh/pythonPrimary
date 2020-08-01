import time

a = time.time()
print(type(a))
print(a)

b = time.strftime('%Y-%m-%d %X')
print(type(b))
print(b)

c = time.strftime('%Y-%m-%d %H:%M:%S')
# c = time.strftime('%Y-%m-%d %H-%M-%S')
print(type(c))
print(c)

# 时间元组:localtime将一个时间戳转换为当前时区的struct_time
d = time.localtime()
print(type(d))
print(d)
print(d.tm_year)
print(d.tm_hour)
print(d.tm_sec)

# time.struct_time(tm_year=2017, tm_mon=7, tm_mday=24,
# 　　　　　　　　　　tm_hour=13, tm_min=59, tm_sec=37, 
#                  tm_wday=0, tm_yday=205, tm_isdst=0)

# 时间戳
t = time.time()

#时间戳-->结构化时间
#time.gmtime(时间戳)    #UTC时间，与英国伦敦当地时间一致
#time.localtime(时间戳) #当地时间。例如我们现在在北京执行这个方法：与UTC时间相差8小时，UTC时间+8小时 = 北京时间 
s1 = time.gmtime(t)
print(s1)
s11 = time.localtime(t)
print(s11)

#结构化时间-->时间戳　
#time.mktime(结构化时间)
t1 = time.mktime(s11)
print(t1)

#结构化时间-->字符串时间
#time.strftime("格式定义","结构化时间")  结构化时间参数若不传，则显示当前时间
t2 = time.strftime("%Y-%m-%d %X")
print(t2)
t22 = time.strftime("%Y-%m-%d %X", s11)
print(t22)

#字符串时间-->结构化时间
#time.strptime(时间字符串,字符串对应格式)
s2 = time.strptime("2017-03-16","%Y-%m-%d")
print(s2)
s22 = time.strptime("07/24/2017","%m/%d/%Y")
print(s22)

#结构化时间 --> %a %b %d %H:%M:%S %Y串
#time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串
t3 = time.asctime(time.localtime(1500000000))
print(t3)
t33 = time.asctime()
print(t33)

#时间戳 --> %a %b %d %H:%M:%S %Y串
#time.ctime(时间戳)  如果不传参数，直接返回当前时间的格式化串
t4 = time.ctime()
print(t4)
t5 = time.ctime(time.time())
print(t5)

# 计算时间差
true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
dif_time=time_now-true_time
struct_time=time.gmtime(dif_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))

from datetime import datetime
#获取当前本地时间
a=datetime.now()
print('当前日期:',a)

#获取当前世界时间
b=datetime.utcnow()
print('世界时间:',b)

#用指定日期创建
c=datetime(2017, 5, 23, 12, 20)
print('指定日期：',c)

d=datetime.strptime('2017/9/30','%Y/%m/%d')
print(d)
e=datetime.strptime('2017年9月30日星期六','%Y年%m月%d日星期六')
print(e)
f=datetime.strptime('2017年9月30日星期六8时42分24秒','%Y年%m月%d日星期六%H时%M分%S秒')
print(f)
g=datetime.strptime('9/30/2017','%m/%d/%Y')
print(g)
h=datetime.strptime('9/30/2017 8:42:50 ','%m/%d/%Y %H:%M:%S ')
print(h)

i=datetime(2017,9,28,10,3,43)
print(i.strftime('%Y年%m月%d日%A,%H时%M分%S秒'))
j=datetime(2017,9,30,10,3,43)
print(j.strftime('%A,%B %d,%Y'))
k=datetime(2017,9,30,9,22,17)
print(k.strftime('%m/%d/%Y %I:%M:%S%p'))
l=datetime(2017,9,30)
print(l.strftime('%B %d,%Y'))

#获取当前系统时间
m=datetime.now()
print(m.strftime('今天是%Y年%m月%d日'))
print(m.strftime('今天是这周的第%w天'))
print(m.strftime('今天是今年的第%j天'))
print(m.strftime('今周是今年的第%W周'))
print(m.strftime('今天是当月的第%d天'))