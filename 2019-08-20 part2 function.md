# 函数

## 概念自测清单

- 参数的传递
- 多参数的传递
- 返回值
- 实参与形参
- 位置参数与关键字参数
- 可变参数
- 变量作用域
- 全局变量与局部变量
- 函数的迭代器和生成器
- 匿名函数以及函数的别称
- 递归函数
- 函数文档
- 模块
- 测试驱动编程
- 可执行程序

## 函数的定义

**函数，实际上是可被调用的完整的程序。是带名字的代码块(Python编程从入门到实践)**它具备输入、处理、输出的功能。又因为它经常在主程序里被调用，所以它总像是个子程序。

函数就是最基本的一种代码抽象的方式，是对程序逻辑进行结构化包装的过程。来源:[函数 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1016959663602400/1017105145133280)

了解一个函数，无非是要了解两个方面

- 输入是什么构成的，有哪些参数，如何指定
- 输出是什么，返回值是什么

### 通过看官方文档了解函数

如何看懂官方文档中对函数的说明？以 print()函数为例。

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


对 Python 内置的函数，可以查看官方文档详细了解：[Built-in Functions — Python 3.7.4rc1 documentation](https://docs.python.org/3/library/functions.html)

**也可以在交互式命令行通过 `help（abs）`查看 `abs`函数的帮助信息。**

如果调用函数输入的参数数量不对，会返回 `TypeError`错误，并且会详细给你指出指引。一定要学会认真看指引。

有了错误指引，搞不定就可以直接复制粘贴去 google ，很多问题其他人都解决过。

### 函数的基本格式是什么？

在Python中，定义一个函数要使用**def语句**，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用`return`语句返回。

首先，要有一个 def （define 定义）关键字，来告诉 Python 你要定义一个函数。

def 后跟上函数的名字。函数取名规范参考变量的取名规范:

- 名称不能以数字开头。能用在名称开头的有，大小写字母和下划线_
- 其次，名称中不能有空格，要么使用下划线连接词汇，如do_nothing，要么使用驼峰命名
- 再次，名称不能与关键词重合——以下是 python 中 Keyword List
	![](https://ws1.sinaimg.cn/large/006tNc79ly1g5qag4sna6j30bw079wew.jpg)
	
变量名后跟着()，指出函数为完成其任务需要什么样的信息。一个函数内部什么都不干（）就为空，但必须带上，以明示它是个函数，而不是某个变量。

()后面的:不要忘了，我经常忘记，提醒一下自己。

冒号后面，紧跟着的所有缩进行构成了**函数体**。

比如:

```
def do_anything():
    print('call me')
    
do_anything()
call me
```

如果想定义一个什么也不做的函数，可以用 `pass`语句。

```
def nop():
    pass
```

 `pass`语句可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个 `pass`，让代码能够运行起来。如果少了 `pass` 代码运行就会有语法问题。


## 输入参数

一个完整的函数，要包含，输入，处理和输出。

在括号内添加参数，就可以让函数接受你给参数指定的任何值。

```
def is_leap(year):
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)
is_leap(300)
```
上面的代码中，year 就是在定义参数，之后可以用 if 语句来给参数设定条件，满足什么条件就执行什么动作。

### 实参与形参

调用函数的过程，将每个实参都关联到函数定义中的一个形参。

year 是形参
300 是实参

他们之间的关系是，在 `is_leap(300)` 中，将实参 300 存储在函数 `is_leap()` 的形参 year中。

### 参数类型与顺序

- 必选参数
- 默认参数
- 可变参数
- 关键字参数
- 命名关键字参数

参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

```
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
```

#### 位置参数、关键字参数以及默认参数

在函数定义中，带有 = 的，即，已为其设定了默认值的参数，叫做 Keyword Arguments（关键字参数），其它的是 Positional Arguments（位置参数）。

位置参数在传递参数的时候位置很重要，实参和形参关联的顺序要保持一致。

为函数的某些参数设定默认值，简化函数的写法。

默认参数有一个坑，如果默认参数的对象是可变对象的时候，重复调用就会出现问题。

```
def add_end(L=[]):
    L.append('END')
    return L
```
当使用默认参数多次调用，就会出现问题。

```python
>>> add_end()
['END']
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
```

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

调整的方法是设置不变对象，None

```
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

关键字参数可以忽略顺序。

### 可变参数


`*args`是可变参数，`args`接收的是一个tuple；
`**kw`是可变关键字参数，kw接收的是一个dict

**可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过`*args`传入：`func(*(1, 2, 3))`；**

可以组装成一个 **tuple** 赋值进去。

```python
def say_hi(*names):
    for name in names:
        print(f'Hi, {name}!')

names = ('mike', 'john', 'zeo')
say_hi(*names)
```

Hi, mike!
Hi, john!
Hi, zeo!

**关键字参数既可以直接传入：`func(a=1, b=2)`，又可以先组装dict，再通过`**kw传入：func(**{'a': 1, 'b': 2})`。**

多个关键字参数的赋值方式需要注意一下。

```
def person(name,age,**kw):
print('name:',name,'age:',age,'other',kw)
person('yushan','25',tall=162,weight=60)
```
name: yushan age: 25 other {'tall': 162, 'weight': 60}

也可以组装成一个**dict**，然后把该 dict 转换为关键字参数传递进去。

```
other = {'tall':162,'weight':60}
person('yushan','25',**other)
```
name: yushan age: 25 other {'tall': 162, 'weight': 60}


**注意**：一个函数中，可以接收一系列值的位置参数只能有一个；并且若是还有其它位置参数存在，**那就必须把这个可以接收一系列值的位置参数排在所有其它位置参数之后**。

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5rh6lalj1j30dr02xdfw.jpg)


### 命名关键字参数

```
def person(name, age, *, city, job):
    print(name, age, city, job)
```

命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

在输出实参时，需要命名。

比如

```
person('Jack', 24, city='Beijing', job='Engineer')
```

### 函数定义时各种参数的排列顺序

在定义函数的时候，各种不同类型的参数应该按什么顺序摆放呢？对于之前写过的 `say_hi()` 这个函数，

```python
def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hi', 'mike', 'john', 'zeo')
say_hi('Welcome', 'mike', 'john', 'zeo', capitalized=True)
```

    Hi, mike!
    Hi, john!
    Hi, zeo!
    Welcome, Mike!
    Welcome, John!
    Welcome, Zeo!

如果，你想给其中的 `greeting` 参数也设定个默认值怎么办？写成这样好像可以：

```python
def say_hi(greeting='Hello', *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hi', 'mike', 'john', 'zeo')
say_hi('Welcome', 'mike', 'john', 'zeo', capitalized=True)
```

    Hi, mike!
    Hi, john!
    Hi, zeo!
    
    Welcome, Mike!
    Welcome, John!
    Welcome, Zeo!

但 `greeting` 这个参数虽然有默认值，可这个函数在被调用的时候，还是必须要给出这个参数，否则输出结果出乎你的想象：

```python
def say_hi(greeting='Hello', *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('mike', 'john', 'zeo')
```

    mike, john!
    mike, zeo!

设定了默认值的 `greeting`，竟然不像你想象的那样是 “可选参数”！所以，你得这样写：

```python
def say_hi(*names, greeting='Hello', capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('mike', 'john', 'zeo')
say_hi('mike', 'john', 'zeo', greeting='Hi')
```

    Hello, mike!
    Hello, john!
    Hello, zeo!
    Hi, mike!
    Hi, john!
    Hi, zeo!

这是因为函数被调用时，面对许多参数，Python 需要按照既定的规则（即，顺序）判定每个参数究竟是哪一类型的参数：

> **Order of Arguments**
> 1. Positional
> 1. Arbitrary Positional
> 1. Keyword
> 1. Arbitrary Keyword

所以，即便你在定义里写成

```python
def say_hi(greeting='Hello', *names, capitalized=False):
    ...
```

在调用该函数的时候，无论你写的是
```python
say_hi('Hi', 'mike', 'john', 'zeo')
```

还是
```python
say_hi('mike', 'john', 'zeo')
```

Python 都会认为接收到的第一个值是 Positional Argument —— 因为在定义中，`greeting` 被放到了 Arbitrary Positional Arguments 之前。

## 处理



## 输出返回值

函数体内部的语句在执行时，一旦执行到`return`时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，类型是 NoneType。

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5riybrmumj30ry0de3zk.jpg)

为什么 第二行 `num = showplus(6)` 的输出结果是 6，按道理说，showplus(6)是执行了 showplus(x)这个函数的结果赋值给 num，而之后打印 num 结果又是 7。

问题：函数的返回值和直接显示输出有什么不同？返回值是函数运行的值，输出值是 print 这个函数运行的结果。

为什么说，返回值能让你将程序的大部分繁重工作一到函数中去完成，从而简化主程序。

调用返回值的函数时，需要提供一个变量，用于储存返回的值。


### 全局变量和局部变量

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

如果希望函数内部的变量变为全局变量，需要加上一个 global 

```python
var = 123
def fun():
    global var = 456
    print(var)
fun()
print(var)
```
这样输出才都是 456


## 函数的迭代器和生成器

详见迭代器和生成器部分。

迭代器，用函数的方式去理解，就是拥有 iter()和 next()两种方法的对象。
生成器，用函数理解，可以是带 yield 的生成器

凡是需要遍历这个效果，就可以用迭代器。

## 练习部分

- 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。

## CHANGELOG
 
 - 20190826 复习完了参数的传递
 - 2019-08-04 继续增补
 

