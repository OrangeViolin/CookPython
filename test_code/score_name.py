# 统计《犯罪心理》中，三名主角出现的次数，刑从连，林辰，王朝。

import re

with open('/Users/yushan/Downloads/《犯罪心理》作者：长洱.txt', 'rt', encoding='GB18030')as f:
     txtall = f.read()
with open('/Users/yushan/Desktop/name.txt', 'rt', encoding='UTF-8') as f:
    namesall = f.read()
def score_name(n):
    namenum = len(re.findall(n, txtall))
    print('主角 %s 出现了 %s 次' % (n, namenum))
names = namesall.split('\n')
for name in names:
    i = 1
    if i %2 != 0:
      print(score_name(name))
    i = i+1