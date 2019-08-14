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

**函数，实际上是可被调用的完整的程序。是带名字的代码块(Python编程从入门到实践)**它具备输入、处理、输出的功能。又因为它经常在主程序里被调用，所以它总像是个子程序。

函数就是最基本的一种代码抽象的方式。来源:[函数 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1016959663602400/1017105145133280)

了解一个函数，无非是要了解两个方面

- 输入是什么构成的，有哪些参数，如何指定
- 输出是什么，返回值是什么

从这个角度，牛对人类来说就是个函数，吃的是草，挤出来的是奶。

当我们在用 python 编程的时候，更多情况下，我们只不过是在使用别人已经写好的函数，或者用更加专业一点的辞藻，叫做“已完好封装的函数”，而我们所需要的事情，通过阅读产品说明书了解如何使用产品。

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

在函数定义中，带有 = 的，即，已为其设定了默认值的参数，叫做 Keyword Arguments，其它的是 Positional Arguments。

对 Python 内置的函数，可以查看官方文档详细了解：[Built-in Functions — Python 3.7.4rc1 documentation](https://docs.python.org/3/library/functions.html)

也可以在交互式命令行通过 `help（abs）`查看 `abs`函数的帮助信息。

一边看，一边多动手试试。

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


## 参数：如何向函数传递信息

一个完整的函数，要包含，输入，处理和输出。

### 接收外部传递进来的值的例子

在括号内添加参数，就可以让函数接受你给参数指定的任何职。

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
        a, b = b, a + b 
        
fib_between(100, 10000)
```
把函数写成返回值是一个列表：

```
def fib_between(start, end):
    r = [] 
    a, b = 0, 1
    while a < end:
        if a >= start:
            r.append(a)
        a, b = b, a + b
    return r
        
fib_between(100, 10000)
```

### 实参和形参

很简单。

```
def is_leap(year):
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)
is_leap(300)
```

year 是形参
300 是实参

他们之间的关系是，在 `is_leap(300)` 中，将实参 300 存储在函数 `is_leap()` 的形参 year中。

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

###  位置参数

位置函数，根据顺序来传递实参。

### 可以接受一系列值的位置参数

如果你在定义参数的时候，在一个*位置参数*（Positional Arguments）前面标注了星号，`*`，那么，这个位置参数可以接收一系列值，在函数内部可以对这一系列值用 `for ... in ...` 循环进行逐一的处理。

带一个星号的参数，英文名称是 “Arbitrary Positional Arguments”，姑且翻译为 “随意的位置参数”。

带两个星号的参数，英文名称是 “Arbitrary Keyword Arguments”，姑且翻译为 “随意的关键字参数”。

![](https://ws3.sinaimg.cn/large/006tNc79ly1g5rg98c0a8j30cb05kdg1.jpg)

为 `for name in names`注明：在定义可以接收一系列值的位置参数时，建议在函数内部为该变量命名时总是用**复数**，因为函数内部，总是需要 `for` 循环去迭代元组中的元素，这样的时候，名称的复数形式对代码的可读性很有帮助。

解释代码：

say_hi()` 这一行没有任何输出。因为你在调用函数的时候，没有给它传递任何值，于是，在函数内部代码执行的时候，`name in names` 的值是 `False`，所以，`for` 循环内部的代码没有被执行。

在函数内部，是把 `names` 这个参数当作容器处理的 —— 否则也没办法用 `for ... in ...` 来处理。而在调用函数的时候，我们是可以将一个容器传递给函数的 Arbitrary Positional Arguments 的 —— 做法是，在调用函数的时候，在参数前面加上星号 `*`

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
实际上，因为以上的 `say_hi(*names)` 函数内部就是把接收到的参数当作容器处理的，于是，在调用这个函数的时候，向它传递任何容器都会被同样处理：

![](https://ws1.sinaimg.cn/large/006tNc79ly1g5rgik4nlnj30fq0i0q4t.jpg)

每一个都会拆分出来，为啥？

拓展：什么是容器？

**注意**：一个函数中，可以接收一系列值的位置参数只能有一个；并且若是还有其它位置参数存在，那就必须把这个可以接收一系列值的位置参数排在所有其它位置参数之后。

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5rh6lalj1j30dr02xdfw.jpg)



## 关键字参数

为函数的某些参数设定默认值，简化函数的写法。

可以在定义函数的时候，为某些参数设定默认值，这些有默认值的参数，又被称作关键字参数（Keyword Argumen）

![](https://ws4.sinaimg.cn/large/006tNc79ly1g5rhjs4xx9j30ij0amdh3.jpg)

在第二次输入的时候我变更了一下关键词参数的默认值。

以及，在第一次写的时候，我没有把`print()`放在`for name in names`这个条件语句下，所以 就没有办法循环了，注意位置呀！


### 可以接受一系列之的关键字参数

可以接收很多值的关键字参数（Arbitrary Keyword Argument）。

![](https://ws3.sinaimg.cn/large/006tNc79ly1g5rhxmkmh3j30ex041wep.jpg)

好神奇，还可以这样设定参数的啊！

这是什么数据类型！

既然在函数内部，我们在处理接收到的 Arbitrary Keyword Argument 时，用的是**对字典的迭代方式**，那么，在调用函数的时候，也可以直接使用字典的形式：

![](https://ws3.sinaimg.cn/large/006tNc79ly1g5ri21f0c4j30ke06ogmb.jpg)

为什么输出的结果是一样的？

![](https://ws4.sinaimg.cn/large/006tNc79ly1g5ri3q7623j30z00esdhu.jpg)

这个没看懂为什么这样处理。



## 函数定义时各种参数的排列顺序

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

## 返回值

#### 函数可以没有返回值【有问题】

函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，类型是 NoneType。

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5riybrmumj30ry0de3zk.jpg)

为什么 第二行 `num = showplus(6)` 的输出结果是 6，按道理说，showplus(6)是执行了 showplus(x)这个函数的结果赋值给 num，而之后打印 num 结果又是 7。

## 练习部分

- 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解。

## CHANGELOG
 
 - 2019-08-04 继续增补
 

