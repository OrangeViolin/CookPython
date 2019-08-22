# 今天学了点啥？

## 20190821

今天最主要还是复习了正则表达式的使用。
对比了 str 对象下的方法和 re 对象下的方法，str 处理字符串往往简单，re 可以处理更加复杂的字符串。

但是对字符串的切分还是感觉没有太掌握。

接触了 any() 这个函数判断，只要有一个为真就会判断为真。
复习了一下列表切片的方法。
复习了一下生成器，写裴波那契数列的前 N 个数

有一种，遇到了问题，自己写代码解决问题的那种快乐。

## 20190820

今天第一部分刷了四道题：[CookPython/2019-08-19 数据结构和算法.md at master · OrangeViolin/CookPython](https://github.com/OrangeViolin/CookPython/blob/master/python3-cookbook/2019-08-19%20%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%92%8C%E7%AE%97%E6%B3%95.md)

给序列解压，我去看了看赋值语句，不难。
给可迭代对象赋值不确定元素数量，可以用星号表达式。
保留最后 N 个元素，可以用 collections 里面的 deque 模块，把可迭代对象变为双向队列对象，可以从前往后截取元素，也可以从后往前截取。
查找最大最小的 N 个元素，用 heapq 模块，尤其适用于那种 N 远远小于对象元素的情况。

梳理了一遍学过的几个概念之间的关系。

- 容器
- 可迭代对象
- 迭代器
- 生成器
- 列表/集合/字典推导式

之间的关系。

理解了一下容器的概念，是多个元素组织在一起的数据结构，Python 标准库中还有很多其他类型的数据结构。

把循环语句看了看，if while for if……else，跳出循环 break，跳过这一次迭代的 continue，占位的 pass ，但我写循环还是很熟练。

