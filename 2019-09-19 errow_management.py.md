# 2019-09-19 异常管理

## 异常定义

错误不等于异常。
错误是代码本身内容，异常是系统对你错误的提示。

## 为啥需要异常管理

自动运行程序对程序错误的异常提示太不友好，你可以替换一种提示方式。

## 看代码

try 跟上你要跑的代码
except 跟上你想要替换的错误类型，exception 可以是所有错误类型
finally 是你最后一定要运行的操作，比如关闭文件


```

try:
    file1 = open('/Users/yushan/Desktop/name.txt', 'w')
    file1.read()
except Exception as m:
    print('你输入错了模式啦 %s' %m)
finally:
    file1.close()
```

输出：

你输入错了模式啦 not readable

注意：Exception 要大写大写大写。

## changelog

- 2019-09-19 创建

