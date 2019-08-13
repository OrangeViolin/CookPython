# advance

## 切片

取一个list或tuple的部分元素是非常常见的操作。

```
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
```

L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

可以从后往前，但倒数第一个元素的索引是-1。

前10个数，每两个取一个：

```
>>> L[:10:2]
[0, 2, 4, 6, 8]
```
所有数，每5个取一个：

```
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
```

## 迭代

Iteration is a general term for taking each item of something, one after another. Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

当我们用一个循环（比如 for 循环）来遍历（一个一个处理）容器（比如列表，元组）中的元素时，这种遍历的过程就叫迭代。

## 列表生成器-do_listcompr

为什么要生成列表？

列表生成式，即 List Comprehensions，是 Python 内置的非常简单却强大的可以用来创建 list 的生成式。

要生成 list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` 可以用 list(range(1,11))

> 注意是 11 包含左边不包含右边

但如果要生成`[1x1, 2x2, 3x3, ..., 10x10]`怎么做？

可以使用循环，最后输出的是列表：

用 print 函数，最后输出的是一个一个的对象。

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5y3w1v85fj30q60b43yz.jpg)

要输出列表，可以考虑用 `append()` 用于在列表末尾添加新的对象。

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5y3xmgflxj30mq06imxg.jpg)

循环太繁琐，列表生成式则可以用一行语句代替循环生成上面的 list：

```
[x*x for x in range(1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
把要生成的元素 `x*x`放在前面，后面跟 `for`循环，就可以把 list 创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

for 后面还可以加上 if 判断，这样我们就可以筛选出仅偶数的平放：

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5y4a5wn1sj30za07440p.jpg)

运用列表生成式，可以写出非常简洁的代码。

```
import os
[d for d in os.listdir('.')]
['.DS_Store', '.git', '.idea', 'data_type.md', 'exe_booklist.md', 'exe_booklist.py', 'function-zip(*iterables).md', 'function.md', 'Git.md', 'Jekyll.md', 'Json.md', 'README.md', 'regex.md', 'shell.md', 'test_Function.py', 'zzh-oh-my-zzh.md', '极客时间编程学习目录.png', '高级特性.md']
```

`for`循环可以同时使用两个甚至多个变量。

![](https://ws1.sinaimg.cn/large/006tNc79ly1g5y4iqwlv3j30ka06kaag.jpg)

那么用 列表生成器也是可以的。

![](https://ws1.sinaimg.cn/large/006tNc79ly1g5y4kg8z0ij30oo0a2gmh.jpg)

items() 返回可遍历的（key，value）元组数组。[Python 字典(Dictionary) items()方法 | 菜鸟教程](https://www.runoob.com/python/att-dictionary-items.html) 

元组中间是冒号，冒号，冒号

### 拓展阅读

OS 模块：[os 模块 - Python 之旅 - 极客学院Wiki](https://wiki.jikexueyuan.com/project/explore-python/File-Directory/os.html) 之后再看

## 生成器

自己去制作一个迭代器，就是生成器。

如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5xa63r8oxj30oo0qwwgd.jpg)

## 迭代器

Iteration（迭代）iterable（可迭代对象） 和 iterator (迭代器)之前的区别是什么


### iterable 可迭代对象

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5x4ovn5ikj30l206sdg0.jpg)

像上面这种可以使用 for 循环进行迭代的对象，就是可迭代对象，它的定义如下:

In Python, iterable and iterator have specific meanings.

An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__ method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no longer valid). So an iterable is an object that you can get an iterator from.

我们可以用 Python 内置的 hasattr() 函数来判断一个对象是不是可迭代：

![](https://ws3.sinaimg.cn/large/006tNc79ly1g5x4w4dws9j30sa0p877r.jpg)

- 数字不是可迭代的对象。
- hasattr()该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。（此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）
- 什么是对象的属性的名称

### iterator 迭代器

能够实现迭代方法的对象就叫做迭代器。

An iterator is an object with a next (Python 2) or __next__ (Python 3) method.

官方介绍：

迭代器是指遵循迭代器协议（iterator protocol）的对象。从这句话我们可以知道，迭代器是一个对象，但比较特别，它需要遵循迭代器协议，那什么是迭代器协议呢？

迭代器协议（iterator protocol）是指要实现对象的 __iter()__ 和 next() 方法（注意：Python3 要实现 __next__() 方法），其中，__iter()__ 方法返回迭代器对象本身，next() 方法返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常。

![](https://ws1.sinaimg.cn/large/006tNc79ly1g5x9eek1icj30rk0m20vb.jpg)


### 小结

- 元组、列表、字典和字符串对象是可迭代的，但不是迭代器，不过我们可以通过 iter() 函数获得一个迭代器对象
- Python 的 for 循环实质上是先通过内置函数 iter() 获得一个迭代器，然后再不断调用 next() 函数实现的
- 自定义迭代器需要实现对象的 __iter()__ 和 next() 方法（注意：Python3 要实现 __next__() 方法），其中，__iter()__ 方法返回迭代器对象本身，next() 方法返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常。

廖雪峰版本总结：

可以直接作用于for循环的数据类型有以下几种：

- 一类是集合数据类型，如list、tuple、dict、set、str等；
- 一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于`for`循环的对象统称为可迭代对象：**Iterable。**

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator


### 额外的解释没看懂

你可能会问，为什么list、dict、str等数据类型不是Iterator？

这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

- 什么是数据流？
- list、dict、str 这些不是迭代器难道不是因为他们本身没有内置函数方法吗？和序列长度有什么关系？

### 参考资料

- [迭代器 (Iterator) - Python 之旅 - 极客学院Wiki](https://wiki.jikexueyuan.com/project/explore-python/Advanced-Features/iterator.html)
- [迭代器 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1016959663602400/1017323698112640)

