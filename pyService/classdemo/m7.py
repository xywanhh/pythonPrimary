import json

# loads和dumps
dic = {'k1':'v1','k2':'v2','k3':'v3'}

# 序列化：将一个字典转换成一个字符串
str_dic = json.dumps(dic)  
print(type(str_dic),str_dic)  
# <class 'str'> {"k3": "v3", "k1": "v1", "k2": "v2"}
# 注意，json转换完的字符串类型的字典中的字符串是由""表示的

# 反序列化：将一个字符串格式的字典转换成一个字典
dic2 = json.loads(str_dic)  
print(type(dic2),dic2)  
# <class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# 注意，要用json的loads功能处理的字符串类型的字典中的字符串必须由""表示

list_dic = [1,['a','b','c'],3,{'k1':'v1','k2':'v2'}]

# 也可以处理嵌套的数据类型 
str_dic = json.dumps(list_dic) 
print(type(str_dic),str_dic) 
# <class 'str'> [1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}]

list_dic2 = json.loads(str_dic)
print(type(list_dic2),list_dic2) 
# <class 'list'> [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]

# load和dump
f = open('E:\\json_file','w')
dic = {'k1':'v1','k2':'v2','k3':'v3'}

# dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
json.dump(dic,f)  
f.close()

# load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
f = open('E:\\json_file')
dic2 = json.load(f)  
f.close()
print(type(dic2),dic2)

# 其他参数
f = open('E:\\file','w')
json.dump({'国籍':'中国'},f)
ret = json.dumps({'国籍':'中国'})
f.write(ret+'\n')
json.dump({'国籍':'美国'},f,ensure_ascii=False)
ret = json.dumps({'国籍':'美国'},ensure_ascii=False)
f.write(ret+'\n')
f.close()

# json的格式化输出
data = {'username':['李华','二愣子'],'sex':'male','age':16}
json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
print(json_dic2)

import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic)
print(str_dic)  #一串二进制内容

dic2 = pickle.loads(str_dic)
print(dic2)    #字典

import time
struct_time  = time.localtime(1000000000)
print(struct_time)
f = open('pickle_file','wb')
pickle.dump(struct_time,f)
f.close()

f = open('pickle_file','rb')
struct_time2 = pickle.load(f)
print(struct_time2.tm_year)

