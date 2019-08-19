# 面向对象惯用法

## 目录

- Object References, Mutability, and Recycling
  - Variables Are Not Boxes
  - Identity, Equality, and Aliases
    - Choosing Between == and is
    - the Relative Immutability of Tuples
  - Copies Are Shallow by Default 
    - Deep and Shallow Copies of Arbitrary Objects
  - Function Parameters and Refernces

## Variables Are Not Boxes

Python 变量类似于 Java 中的**引用式变量**，因此最好把它们理解为附加在对象上的标注。

比如，变量 a 和 变量 b 引用同一个列表，而不是那个列表的副本。

```
a = [1,2,3]
b = a 
a.append(4)
b
```
输出：[1,2,3,4]

描述方式的严谨：对引用式变量来说，说吧变量分配给对象更加合理，反过来说就有问题，毕竟，对象在复制之前就创建了。

创建对象之后才会把变量分配给对象。

```
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))
x = Gizmo() 
```
输出：Gizmo id：4301489152

### 其他拓展，关于 %的变量置入字符：

对于整数，是取余数运算。
对于字符串，是c风格的字符串**格式化**运算。字符串格式化，string formatting

简单的说，这是一种将其他变量置入字符串特定位置以生成新字符串的操作，比如说:
```
n = "Aki"
"My name is %s" % n
```
这段代码首先把变量 n 分配给了对象 Aki。然后下方的字符串中有一个%s，他的含义是“这里将被替换成一个新的字符串”，用作替换的内容放在字符串后面的%后面，就是那个n。

所以最终这个字符串会变成 My name is Aki。字符串中的%后面会附带一个字母，代表着用来替换的变量的类型，比如说%d代表着你将替换到此处的变量是一个整数，而%s代表着一个字符串。详细细节可在这里看到。

- [Python中%是什么意思？如何使用？ - 知乎](https://www.zhihu.com/question/54933434/answer/142187767)
- [5. Built-in Types — Python 2.7.16 documentation](https://docs.python.org/2/library/stdtypes.html#string-formatting-operations)

### TODO

- 为什么要格式化？主要是解决哪些问题？
- 格式化有哪些规则？

## == and is
  
 ![](https://ws4.sinaimg.cn/large/006tNc79ly1g65bnqpfe6j30we0l0mz2.jpg)

b 是 a 的别名，两个变量绑定同一个对象。
a 和 b 绑定同一个对象，c 绑定的对象具有相同的内容，具有相同的值，== 比较的是值，但是他们的标识不同。

每个变量都有标识、类型和值。对象一旦创建，它的标识绝不会变，你可以把标识理解为对象在内存中的地址。is 运算符比较两个对象的标识；id() 函数返回对象标识的整数表示。ID 一定是一个唯一的数值标注，而且在对象的生命周期中绝不会变。

### == 和 is 之间的选择

== 比较两个对象的值，而 is 比较对象的标识。

如何选择？

is 效率优于 ==，因为 is 操作符无法被重载，执行 is 操作符只要对对象的 ID 进行比较，而 == 操作符则会递归地遍历对象的所有值。




