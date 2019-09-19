#file1 = open('/Users/yushan/Desktop/name.txt',w)
#file1.read()

try:
    file1 = open('/Users/yushan/Desktop/name.txt', 'w')
    file1.read()
except Exception as m:
    print('你输入错了模式啦 %s' %m)
finally:
    file1.close()