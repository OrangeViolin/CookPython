# 2019-08-20 collections — Container datatypes

这个模块实现了特定目标的容器，以提供 Python 标准内建容器 dict、list、set 和 tuple 的替代选择。

[collections --- 容器数据类型 — Python 3.7.4 文档](https://docs.python.org/zh-cn/3/library/collections.html)

## deque 对象

class collections.deque([iterable[, maxlen]])

返回一个新的双向队列对象，从左到右初始化（用方法 append()）,用 iterable 数据创建，如果 iterable 没有指定，新队列为空。

内存高效添加(append)和弹出(pop)，从两端都可以。

对象支持以下方法：

* append(x)添加 x 到右端。
* appendleft(x)添加 x 到左端。
* clear()移除所有元素，使其长度为0.
* copy()创建一份浅拷贝。
* count(x)计算deque中个数等于 x 的元素。
* extend(iterable)扩展deque的右侧，通过添加iterable参数中的元素。
* extendleft(iterable)扩展deque的左侧，通过添加iterable参数中的元素。注意，左添加时，在结果中iterable参数中的顺序将被反过来添加。
* index(x[, start[, stop]])返回第 x 个元素（从 start 开始计算，在 stop 之前）。返回第一个匹配，如果没找到的话，升起 ValueError 。
* insert(i, x)在位置 i 插入 x 。如果插入会导致一个限长deque超出长度 maxlen 的话，就升起一个 IndexError 。
* pop()移去并且返回一个元素，deque最右侧的那一个。如果没有元素的话，就升起 IndexError 索引错误。
* popleft()移去并且返回一个元素，deque最左侧的那一个。如果没有元素的话，就升起 IndexError 索引错误。
* remove(value)移去找到的第一个 value。 如果没有的话就升起 ValueError 。
* reverse()将deque逆序排列。返回 None 。
* rotate(n=1)向右循环移动 n 步。 如果 n 是负数，就向左循环。
* 如果deque不是空的，向右循环移动一步就等价于d.appendleft(d.pop()) ， 向左循环一步就等价于 d.append(d.popleft()) 。Deque对象同样提供了一个只读属性:
* maxlenDeque的最大尺寸，如果没有限定的话就是 None 。

除了以上，deque还支持迭代，清洗，len(d), reversed(d), copy.copy(d), copy.deepcopy(d), 成员测试 in 操作符，和下标引用 d[-1] 。索引存取在两端的复杂度是 O(1)， 在中间的复杂度比 O(n) 略低。要快速存取，使用list来替代。


