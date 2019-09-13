# 错题记录

记录我各种各样的错误吧

## 函数使用出错

### os 模块

```
[for x in os.listdir('.') if os.path.split[1]='.py' ]
```
- 我没有给 os.path.split 函数赋值呀
- 判断字符串里面是否有一个字符串，用 == 而不是 = 
- 要分离文件名和扩展名要用 os.path.splitext
- 列表生成式也有很多错误，漏掉最开始的 x 了

### open()

写 rt 参数没有添加单引号
read 函数，fileObject.read(),参数是 size，空格也算是一个字节。

用完了 rt模式 之后再用一次 at 模式，就不行了。

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6mmfb2h1fj30va0sw3zu.jpg)
不是不行了，而是 at 模式下，就是不能读取，而是写入啊！

## 循环函数

if 语句不是循环。

写循环语句，常用一个中间变量 n 来控制循环条件，这样比较简洁能够表达循环语句的关系。

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

