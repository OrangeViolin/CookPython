# 2019-09-26 ResumeExtract

## 任务定义

输入：一堆 jason 格式的文件，网络上爬取的数据

输出：把没有提对的出生日期替换掉，仍旧保存为 json 格式的文件

- 完整格式：XXXX年XX月XX日
- 没有日：XXXX年XX月
- 没有年：XXXX年

## 解决思路

任务拆解：

- 读取数据
- 提取数据
- 替换数据
- 写入数据

解决思路：

- 用 pandas 的 read_json函数可以将json数据转化为dataframe
- 用正则匹配
- 匹配到就放到一个list
- 用 pandas to_json 写入到 json

问题记录

- 怎么使用 pandas 读取数据？google pandas   json 详见：[pandas]()
  - pandas里的read_json函数可以将json数据转化为dataframe。 
  - OS 模块下用 os.listdir 以及 os.path.abspath 读取文件夹下所有文件的路径
  - 用 for 循环一个一个解析
  - 将数据保存在变量中

但感觉现在这样，我不知道要如何定位到要提取那一段文本，提取的结果，还要保存到一个特定的列，但是按照现在提取的颗粒度，基本上是不足够的。

## 


## ref

- [pandas处理json数据_ITPUB博客](http://blog.itpub.net/26736162/viewspace-2647241/)
- [pandas.read_json — pandas 0.25.1 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)

