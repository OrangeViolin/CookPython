# function-zip(*iterables)

Make an iterator that aggregates elements from each of the iterables.

创建一个聚合了来自每个可迭代对象中的元素的迭代器。

Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator. 

输入是一个可迭代对象，返回是一个**元组的迭代器**。带上星号表示这是可变的参数。**其中，第 i 个元组包含来自每个参数序列或可迭代对象的第 i 个元素。**当所输入可迭代对象中最短的一个被耗尽时，迭代器将停止迭代。当只有一个可迭代对象参数时，它将返回一个单元组的迭代器。不带参数时，它将返回一个空迭代器。

我们可以使用 list() 转换来输出列表。

注意：zip 函数在 python2 输出的是列表，但是 python3 中输出的是迭代器，需要用 list()转换来输出列表。

也就是说，把每个迭代器中同一位置的元素拼成一个元组的迭代器啊。

![](https://ws2.sinaimg.cn/large/006tNc79ly1g5x5w1gtu4j30qy0jg76s.jpg)

问题：

- 为什么 zip 的输出值，数据类型是 zip？ zip 是一种数据类型？

zip() 与 `*` 运算符相结合可以用来拆解一个列表。

![](https://ws4.sinaimg.cn/large/006tNc79ly1g5x81ilhr8j30x50u0gqg.jpg)

问题：

- zipped 也是一个可迭代对象，为什么 `x2, y2 = zip(*zipped)`以及`x2, y2 = zip(zipped)`会报错呢？ `zip(x,y)`的值不是已经赋给了 `zipped` 了吗？


