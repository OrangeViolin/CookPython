# 错题记录

记录我各种各样的错误吧

## 循环函数

> 把 return 语句写在了循环代码块当中，导致循环只能够执行一遍。

错误的版本
```
def power (x,n):
    s = 1
    while n >= 0:
        n = n -1
        s = s * x
        return s
    
print(power (5,2))
5
```
正确版本
```
def power (x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s 
power(5,2)
25
```
## changelog

- 20190827 创建

