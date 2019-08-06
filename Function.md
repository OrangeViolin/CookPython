# 函数

函数涉及的话题有

- 参数的传递
- 多参数的传递
- 匿名函数以及函数的别称
- 递归函数
- 函数文档
- 模块
- 测试驱动编程
- 可执行程序

## 函数的定义

**函数，实际上是可被调用的完整的程序。**它具备输入、处理、输出的功能。又因为它经常在主程序里被调用，所以它总像是个子程序。

了解一个函数，无非是要了解两个方面

- 输入是什么构成的，有哪些参数，如何指定
- 输出是什么，返回值是什么

从这个角度，牛对人类来说就是个函数，吃的是草，挤出来的是奶。

当我们在用 python 编程的时候，更多情况下，我们只不过是在使用别人已经写好的函数，或者用更加专业一点的辞藻，叫做“已完好封装的函数”，而我们所需要的事情，通过阅读产品说明书了解如何使用产品。

官方文档：[Built-in Functions — Python 3.7.4rc1 documentation](https://docs.python.org/3/library/functions.html)

如何看懂官方文档中对函数的说明？

print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)

- sep=' '：接收多个参数之后，输出时，分隔符号默认为空格，' '；

  ```
  print('I am YuShan', sep=';')
  I am YuShan
  print('I am YuShan','I am in China', sep=';')
  I am YuShan;I am in China
  ```
  
- end='\n'：输出行的末尾默认是换行符号 '\n'；
- file=sys.stdout：默认的输出对象是 sys.stdout（即，用户正在使用的屏幕）……
- flush=False flush=False： 该参数主要是刷新， 默认False，不刷新，Ture时刷新

函数的返回值和向屏幕输出的内容不一样。

print() 这个函数的返回值是 None 但向屏幕输出的内容即输入的内容。

在函数定义中，带有 = 的，即，已为其设定了默认值的参数，叫做 Keyword Arguments，其它的是 Positional Arguments。

## 参数

一个完整的函数，要包含，输入，处理和输出。

### 函数的取名

一个函数内部什么都不干，也得有个名字，然后名字后面要加上圆括号（），以明示它是个函数，而不是某个变量。

定义一个函数的关键字是 def，圆括号内为空即一个什么都不干的函数。

```
def do_anything():
    print('call me')
    
do_anything()
call me
```

参考变量的取名规范。

- 名称不能以数字开头。能用在名称开头的有，大小写字母和下划线_
- 其次，名称中不能有空格，要么使用下划线连接词汇，如do_nothing，要么使用驼峰命名
- 再次，名称不能与关键词重合——以下是 python 中 Keyword List
	![](https://ws1.sinaimg.cn/large/006tNc79ly1g5qag4sna6j30bw079wew.jpg)
	
	

### 函数可以没有返回值

函数内部，不一定非要有 return 语句。但如果函数内部并未定义返回值，那么函数的返回值是 None，当 None 被当做布尔值对待的时候，相当于是  False

怎么知道函数是否有返回值？

返回值简介

- 简单介绍 print 和 return 的区别，print 仅仅是打印在控制台，而 return 则是将 return 后面的部分作为返回值作为函数的输出，可以用变量接走，继续使用该返回值做其它事。
- 函数需要先定义后调用，函数体中 return 语句的结果就是返回值。如果一个函数没有 reutrn 语句，其实它有一个隐含的 return 语句，返回值是 None，类型也是 'NoneType'。
- return 语句的作用：结束函数调用、返回值

指定返回值与隐含返回值

- 函数体中 return 语句有指定返回值时返回的就是其值
- 函数体中没有 return 语句时，函数运行结束会隐含返回一个 None 作为返回值，类型是 NoneType，与 return 、return None 等效，都是返回 None。

```
def showplus(x):
    print(x)
    return x + 1

num = showplus(6)
add = num + 2
print(add)

输出结果：

6
9
```

隐含 return None 举例：

```
def showplus(x):
    print(x)

num = showplus(6)
print(num)
print(type(num)) 

输出结果：
6
None
<class 'NoneType'>

```

```
def showplus(x):
    print(x)
    return x+1
hey = showplus(8)
8
print(hey)
9
type(print(hey))
9
<class 'NoneType'>
```
## 接收外部传递进来的值

写一个判断闰年年份的函数。

闰年的定义

- 年份能被 4 整除
- 年份能被 100 整除却不能被 400 整除

```
def is_leap(year):
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)
is_leap(300)
False
is_leap(400)
True
type(is_leap(400))
<class 'bool'>
```
上面的代码中，year 就是在定义参数，之后可以用 if 语句来给参数设定条件，满足什么条件就执行什么动作。

也可以定义多个参数。

练习：写个函数，让它输出从大于某个数字到小于另外一个数字的斐波那契数列

```
def fib_between(start, end):
    a, b = 0, 1
    while a < end: #a 小于 end 开始执行
        if a >= start: #如果 a 大于 start 
            print(a, end=' ') # 输出结果
        a, b = b, a + b # 这一行是什么？
        
fib_between(100, 10000)
```
把函数写成返回值是一个列表：

```
def fib_between(start, end):
    r = [] #这一行也没看懂，为啥能这样定义？
    a, b = 0, 1
    while a < end:
        if a >= start:
            r.append(a)
        a, b = b, a + b
    return r
        
fib_between(100, 10000)
```

## 变量作用阈

```
def increase_one(n):
    n += 1
    return n
n = 1
print(increase_one(n))
2
print(n)
1
```

+= 表示两个值相加，把结果赋给左边的变量。

print(n)还是 1，为啥？

首先，每次某个函数被调用的时候，这个函数会开辟一个新的区域，这个函数内部所有的变量，都是局域变量。也就是说，即便那个函数内部某个变量的名称与它外部的某个全局变量名称相同，它们也不是同一个变量 —— 只是名称相同而已。

其次，更为重要的是，**当外部调用一个函数的时候，准确地讲，传递的不是变量，而是那个变量的值。**也就是说，当 increase_one(n) 被调用的时候，被传递给那个恰好名称也叫 n 的局域变量的，是全局变量 n 的值，1。

而后，increase_one() 函数的代码开始执行，局域变量 n 经过 n += 1 之后，其中存储的值是 2，而后这个值被 return 语句返回，所以，print(increase(n)) 所输出的值是函数被调用之后的返回值，即，2。

然而，全局变量 n 的值并没有被改变，因为局部变量 n（它的值是 2）和全局变量 n（它的值还是 1）只不过是名字相同而已，但它们并不是同一个变量。







