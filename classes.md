# 类——面向对象编程

## 面向对象编程

这不是专属于哪个编程语言（比如 Python、JavaScript 或者 Golang）

面向对象编程（Object Orieneted Programming,OPP)是一种编程的范式（Paradigm），或者说，是一种方法论（Methodology）现代软件工程能做那么复杂的宏伟项目，基本上都得益于这个方法论的普及。

【待深入了解】

## 争议

面向对象编程也存在一些争议。

Erlang 的发明者，Joe Armstrong) 就很讨厌 OOP，觉得它效率低下。他用的类比也确实令人忍俊不禁，说得也挺准的：

> 支持 OOP 的语言的问题在于，它们总是随身携带着一堆并不明确的环境 —— 你明明只不过想要个香蕉，可你所获得的是一个大猩猩手里拿着香蕉…… 以及那大猩猩身后的整个丛林！—— Coders at Work

创作 UTF-8 和 Golang 的程序员 Rob Pike，更看不上 OOP，在 2004 年的一个讨论帖里直接把 OOP 比作 “Roman numerals of computing” —— 讽刺它就是很土很低效的东西。八年后又挖坟把一个 Java 教授写的 OOP 文章嘲弄了一番：“也不知道是什么脑子，认为写 6 个新的 Class 比直接用 1 行表格搜索更好？”

Paul Graham —— 就是那个著名的 Y-Combinator 的创始人 —— 也一样对 OOP 不以为然，在 Why Arc isn't Especially Object-Oriented 中，说他认为 OOP 之所以流行，就是因为平庸程序员（Mediocre programers）太多，大公司用这种编程范式去阻止那帮家伙，让他们捅不出太大的娄子……

然而，争议归争议，应用归应用 —— 就好像英语的弊端不见得比其他语言少，可就是最流行，那怎么办呢？用呗 —— 虽然该抱怨的时候也得抱怨抱怨。

从另外一个角度望过去，大牛们如此评价 OOP 也是很容易理解的 —— 因为他们太聪明，又因为他们太懒得花时间去理解或容忍笨蛋…… 我们不一样，最不一样的地方在于，我们不仅更多容忍他人，而且更能够容忍自己的愚笨，所以，视角就不同了，仅此而已。

【这些争议背后的原因，也想认认真真去看一看】

## 基本术语

- 对象
- 封装
- 抽象
- 界面
- 属性
- 方法
- 继承
- 类
- 子类
- 实例

面向对象编程(OOP)，是使用**对象**(Objects)作为核心的编程方式，进而就可以把对象的数据和运算过程**封装**在内部，而外部仅能根据事先设计好的**界面**与之沟通。

比如，你可把灯泡想象成一个对象(Object)，使用灯泡的人，只需要与开关这个界面(interface)打交道，而不必关心灯泡内部的设计和原理。

在程序设计过程中，我们常常需要对标显示世界创造对象。这时候我们用的最直接手段就是**抽象**（Abstract）。

必要特征，叫做对象的**属性**。
必要行为，叫做对象的**方法**。

我们在程序里创建对象的时候，通常的做法常常是

- 先创建最抽象的类
- 然后再创建子类

他们之间的从属关系是，子类属于类，这叫做继承关系。

每当我们创建好一个类之后，我们就可以根据它创建许多个**实例（Instance）**，比如创建好了狗这个类，我们就可以根据这个类创建很多条狗，这好多条狗，就是狗这个类的实例。

## Defining Class

Class 使用 class 关键字进行定义。

与函数定义不同的地方在于，Class 接收参数不是在 class Classname(): 的括号里完成 —— 那个圆括号有另外的用处。


![](https://ws1.sinaimg.cn/large/006tNc79ly1g647xgw0xtj30zo0n877m.jpg)

我们创建了一个 Class：

```
class Golem:

    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year

```

这里定义了，当我们根据这个 Class 创建一个 实例的时候，那个 Object 的初始化过程，即 __init__() 函数，这个函数是在 Class 中定义的，我们称它为 Class 的一个 Method。

这里的 self 就是个变量，跟程序中其他变量的区别在于，它是一个系统默认可以识别的变量，**用来指代将来用这个 Class 创建的 Instance。** 这样，之后的 Instance 就可以调用 Class 中的方法。

比如，我们创建了 Golem 这个 Class 的一个 Instance，g = Golem('Clay')之后，我们写 g.name,那么计时器就会去找 g 这个实例所在的 Scope 里面有没有 self.name

在 Class 的代码中，如果定义了 `__init__()` 函数，那么系统就会将它当做 Instance 在创建后初始化的函数。这个函数名称是强制制定的，初始化函数必须使用这个名称。

当我们用 g = Golem('Clay') 这一句创建了一个 Golem 的 Instance 的时候，以下一连串的事情发生了：

- g 从此以后就是一个根据 Golem 这个 Class 创建的 Instance，**对使用者来说，它就是个 Object**
- 因为 Golem 这个 Class 的代码中有 `__init__()`，所以，当 g 被创建的时候，g 就需要被初始化
- 在 g 所在的变量目录中，出现了一个叫做 self 的用来替代 g 本身的变量
- self.name 接受了一个参数，'Clay'，并将它保存下来
- 生成了一个  self.built_year 的变量，其中保存的是 g 这个额 Object 被创建时的年份

## Inheritance

我们创建了一个 Golem Class ，如果我们相拥它 Inherite 一个新的 Class，比如，Running_Golem，一个能跑的机器人，那就像以下的代码那样做。

注意 class Running_Golem 之后的圆括号：

![](https://ws3.sinaimg.cn/large/006tNc79ly1g648fozli4j31140diaby.jpg)

因为它是 Golem 的 Inheritance，那么 Golem 有的 Attributes 和 Methods 它都有，并且还多了一个 Method—— self.run。

## Overrides

当我们创建一个  Inherited Class 的时候，可以重写 Parent Class 中的 Methods。

![](https://ws1.sinaimg.cn/large/006tNc79ly1g648kd9wasj31180f2gnj.jpg)

## Inspecting A Class

当我们作为用户想了解一个 Class 的 Interface，即，它的 Attributes 和 Methods 的时候，常用的三种方式：

1. help(object)
2. dir(object)
3. object.___dict__

![](https://ws2.sinaimg.cn/large/006tNc79ly1g648p6g7vdj311y0sq0w0.jpg)

## Scope 

 每个变量都属于某一个 Scope（变量的作用域），在同一个我们先给 Golem 这个 Class 增加一点功能 —— 我们需要随时知道究竟有多少个 Golem 处于活跃状态…… 也因此顺带给 Golem 加上一个 Method：cease() —— 哈！机器人么，想关掉它，说关掉它，就能关掉它；

另外，我们还要给机器人设置个使用年限，比如 10 年；

…… 而外部会每隔一段时间，用 Golem.is_active() 去检查所有的机器人，所以，不需要外部额外操作，到了年头，它应该能关掉自己。—— 当然，又由于以下代码是简化书写的，核心目的是为了讲解 Scope，所以并没有专门写模拟 10 年后某些机器人自动关闭的情形……

在运行以下代码之前，需要先介绍三个 Python 的内建函数：

- hasattr(object, attr) 查询这个 object 中有没有这个 attr，返回布尔值
- getattr(object, attr) 获取这个 object 中这个 attr 的值
- setattr(object, attr, value) 将这个 object 中的 attr 值设置为 value

## Changelog

- 20190818 基本了解了 类 的概念

