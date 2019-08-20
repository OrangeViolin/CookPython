# 2019-08-20 heapq — Heap queue algorithm

[heapq --- 堆队列算法 — Python 3.7.4 文档](https://docs.python.org/zh-cn/3/library/heapq.html?highlight=heapq#module-heapq)

这个模块提供了堆队列算法的实现，也成为优先队列算法。

堆是一个二叉树，它的每个父节点的值都只会大于或小于所有子节点的值。它使用了数组来实现：从零开始计数，对于所有的k，都有``heap[k]<=heap[2*k+1]`` 和 ``hepa[k]<=heap[2*k+2``。为了便于比较，不存在的元素被认为是无限大。堆最有趣的特性自傲与最小的元素总是在根节点：heap[0]

定义了以下函数：

heapq.heappush(heap, item)
将 item 的值加入 heap 中，保持堆的不变性。

heapq.heappop(heap)
弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。

heapq.heappushpop(heap, item)
将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率。

heapq.heapify(x)
将list x 转换成堆，原地，线性时间内。

heapq.heapreplace(heap, item)
Pop and return the smallest item from the heap, and also push the new item. The heap size doesn't change. If the heap is empty, IndexError is raised.

This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.

The value returned may be larger than the item added. If that isn't desired, consider using heappushpop() instead. Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.

The module also offers three general purpose functions based on heaps.

**heapq.merge(*iterables, key=None, reverse=False)**
Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.

Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).

具有两个可选参数，它们都必须指定为关键字参数。

key specifies a key function of one argument that is used to extract a comparison key from each input element. The default value is None (compare the elements directly).

reverse is a boolean value. If set to True, then the input elements are merged as if each comparison were reversed. To achieve behavior similar to sorted(itertools.chain(*iterables), reverse=True), all iterables must be sorted from largest to smallest.

在 3.5 版更改: Added the optional key and reverse parameters.

**heapq.nlargest(n, iterable, key=None)**

Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key, reverse=True)[:n].

**heapq.nsmallest(n, iterable, key=None)**

Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable (for example, key=str.lower). Equivalent to: sorted(iterable, key=key)[:n].

The latter two functions perform best for smaller values of n. For larger values, it is more efficient to use the sorted() function. Also, when n==1, it is more efficient to use the built-in min() and max() functions. If repeated usage of these functions is required, consider turning the iterable into an actual heap.

