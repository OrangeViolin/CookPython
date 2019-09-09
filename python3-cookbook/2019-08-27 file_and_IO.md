# 2019-08-27 file_and_IO

## 用open 函数的 rt，wt 和 at 模式读写文本数据

### 问题

你需要读写各种不同编码的文本数据，比如ASCII，UTF-8或UTF-16编码等。

### 解决方案

### 读取，写入以及添加至文件中

熟悉 open()方法中的，rt，wt 和 at

读取：r
写入：w
添加：at

### 读取

使用带有 rt 模式的 `open()` 函数读取文本文件,read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。如下所示：

```python
# 将文件读取为字符串
with open('somefile.txt', 'rt') as f:
    data = f.read()
```
为了写入一个文本文件，使用带有 wt 模式的 open() 函数，如果之前文件内容存在则清除并覆盖掉。

### 写入

`wt`模式下，可以用 fileObject.write(text) 也可以用 print(line,file=fileObject)

```python
#写入文本，并且把之前的内容覆盖掉
with open('somefile.txt', 'wt') as f:
    f.write(text1)
    f.write(text2)

with open('/Users/yushan/Desktop/selflearning.txt','wt') as f:
    print('yushanyushan',file=f)
    print('relaxrelax',file=f)
```
如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数。

```python
with open('/Users/yushan/Desktop/selflearning.txt','at') as f:
    a = f.write('hey,come on.')
    print(a)
```
12
输出的结果是写入的字节数。

### 在文件读取后用循环

for line in f

```python
with open('/Users/yushan/Desktop/selflearning.txt','rt') as f:
    for line in f:
        print(line)
```
hey,come on.
 hey,come on.

### open 函数的 errors 参数如何解决编码错误

先去看看编码，给 encoding 参数定好参数，或者使用 latin-1，实在不行就给 errors 参数赋值。

'replace'会将解码不了的，替换成问号。
'ignore'会将解码不了的，直接略过。

##  print 函数

### 打印输出至文件中

你想将 print()函数的输出重定向到一个文件中去。

### 解决方法

在 print()函数中指定 file 关键字参数。

```python
with open('/Users/yushan/Desktop/somefile.txt','wt')as f:
    print('hello yushan',file=f)
```

### print 函数中使用其他分隔符或行终止符打印

你想使用 print() 函数输出数据，但是想改变默认的分隔符或者行尾符。

```python
print('ACME', 50, 91.5,sep=';',end='hhh')
```
ACME;50;91.5hhh

## 用 wb 和 rb 模式来读写字节数据

### 问题

你想读写二进制文件，比如图片，声音文件等等。

### 解决方法

open()函数中模式为 rb 或者 wb 

注意，用 write()方法来写入文件，注意要加上限定：
```python
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')
```
在读取二进制数据时，需要指明的是所有返回的数据都是字节字符串格式的，而不是文本字符串。 类似的，在写入的时候，必须保证参数是以字节形式对外暴露数据的对象(比如字节字符串，字节数组对象等)。

索引和迭代动作返回的是字节的值而不是字节字符串:

```python
>>> # Text string
>>> t = 'Hello World'
>>> t[0]
'H'
>>> for c in t:
...     print(c)
...
H
e
l
l
o
...
>>> # Byte string
>>> b = b'Hello World'
>>> b[0]
72
>>> for c in b:
...     print(c)
...
72
101
108
108
111
...
>>>
```

## 用 xt 模式来检查文件是否存在

### 问题

你想向一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。 也就是不允许覆盖已存在的文件内容。

### 解决方法

可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题。

用 xt 来检查文件是否存在，如果文件存在就会返回错误。

```
FileExistsError: [Errno 17] File exists: '/Users/yushan/Desktop/selflearning.txt'
```

## 字符串的I/O操作：StringIO 和 BytesIO 在内存中读写

### 问题

你想使用操作类文件对象（其实就是类似于文件的对象）的程序来操作文本或二进制字符串。

意思就是在内存中读写。

### 解决方法

使用 StringIO 或者 BytesIO 的方法。**类文件对象。**

`io.StringIO()`和`io.BytesIO()`

用 Object.getvalue() 来读取文件。

```python
b = io.StringIO()
b.write('yushanyushan\n')
b.getvalue()
```
'yushanyushan\n'

要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取

```python
c = io.StringIO('YUSHAN')
c.read()
```
'YUSHAN'

当你想模拟一个普通的文件的时候 StringIO 和 BytesIO 类是很有用的。 比如，在单元测试中，你可以使用 StringIO 来创建一个包含测试数据的类文件对象， 这个对象可以被传给某个参数为普通文件对象的函数。

需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用。

## 用 os 模块操作文件和目录

操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中。

### 问题

利用os模块编写一个能实现dir -l输出的程序。


### 问题

编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

### 解决方法

更细化一下问题，找出文件名包含 .py 的文件并且打印出来

```python
[x for x in os.listdir('.') if os.path.splitext(x)[1]=='.py' ]
```
['test_Function.py', 'exe_booklist.py']

## changelog

- 2019-09-03 复习了一遍对 open 函数的操作

