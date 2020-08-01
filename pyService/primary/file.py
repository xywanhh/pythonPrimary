
f = open('1.txt', mode='r', encoding='utf-8')
# c1 = f.read()
l1 = f.readline().strip()
# print(c1)
print(l1)
f.close()

f1 = open('./2.txt', mode='w', encoding='utf-8')
f1.write('11111')
f1.write('22222')
f1.flush()
f1.close()

f2 = open('./3.txt', mode='a', encoding='utf-8')
f2.write('11111\n')
f2.write('22222\n')
f2.flush()
f2.close()

# jpg file
# j1 = open('c:/1.jpg', mode='rb')
# j2 = open('d:/1.jpg', mode='wb')
# for line in j1:
#     j2.write(line)
# j1.close()
# j2.flush()
# j2.close()